from typing import Type, Optional

from fastapi import status
from fastapi.responses import JSONResponse

from .handler import ControllerBase, Request

from ...application.dtos import ArticleRequestDto
from ...application.usecases import CreateArticleUsecase
from ...infrastructure.repositories import ArticleRepository


class CreateArticleController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""

        article_usecase = CreateArticleUsecase(ArticleRepository())
        resp = await article_usecase.execute(ArticleRequestDto(
            request.body.get('title'), request.body.get('url'),
            request.body.get('summary'), request.body.get('featured'),
            request.body.get('image_url'), request.body.get('news_site')
        ))

        if resp.error_value():
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=dict(
                    message=str(resp.error_value().message)
                )
            )

        if resp.get_value().status == 200:
            return request.body
