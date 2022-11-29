from typing import Type, Optional

from fastapi import status
from fastapi.responses import JSONResponse

from .handler import ControllerBase, Request

from ...application.usecases import DeleteArticleUsecase
from ...infrastructure.repositories import ArticleRepository


class DeleteArticleController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""

        article_usecase = DeleteArticleUsecase(ArticleRepository())
        resp = await article_usecase.execute(request.params[0])

        if resp.error_value():
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=dict(
                    message=str(resp.error_value().message)
                )
            )

        if resp.get_value().status == 200:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=dict(
                    message=str(resp.get_value().message)
                )
            )
