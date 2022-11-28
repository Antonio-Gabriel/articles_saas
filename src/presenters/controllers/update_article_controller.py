from typing import Type, Optional

from fastapi import status
from fastapi.responses import JSONResponse

from .handler import ControllerBase, Request

from ...application.dtos import ArticleRequestDto
from ...application.usecases import UpdateArticleUsecase
from ...infrastructure.repositories import ArticleRepository


class UpdateArticleController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""
        article_usecase = UpdateArticleUsecase(ArticleRepository())
        resp = await article_usecase.execute(ArticleRequestDto(
            request.body.get('title'), request.body.get('url'),
            request.body.get('summary'), request.body.get('featured'),
            request.body.get('image_url'), request.body.get('news_site')
        ), request.params[0])

        if resp.error_value():

            error_response: dict(int, dict) = {
                404: {
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "content": dict(
                        message=str(resp.error_value().message)
                    )
                },
                400: {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "content": dict(
                        message=str(resp.error_value().message)
                    )
                }
            }

            err_resp = error_response\
                .get(resp.error_value().status, None)

            return JSONResponse(
                status_code=err_resp["status_code"],
                content=err_resp["content"]
            )

        if resp.get_value().status == 200:
            return request.body
