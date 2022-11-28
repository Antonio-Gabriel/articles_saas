import os
from uuid import UUID
from fastapi import APIRouter, status
from fastapi_pagination import Page, add_pagination, LimitOffsetPage, paginate

from .formatter import format_articles_responses

from ..schemas import ArticleSchemaReponse
from ...controllers import (
    GetArticlesController,
    GetArticleByIdController,
    Request)

article_route = APIRouter(prefix=os.environ["BASE_PATH"], tags=["Article"])


@article_route.get("/articles",
                   status_code=status.HTTP_200_OK,
                   response_model=Page[ArticleSchemaReponse],
                   response_description="Get all articles paginated")
@article_route.get("/articles/limit-offset",
                   status_code=status.HTTP_200_OK,
                   response_model=LimitOffsetPage[ArticleSchemaReponse],
                   response_description="Get all articles paginated")
async def get_articles():
    """get all articles"""
    article_controller = GetArticlesController()
    articles = await article_controller.handle()
    response = format_articles_responses(articles)

    return paginate(response)

add_pagination(article_route)


@article_route.get("article/{article_id}",
                   status_code=status.HTTP_200_OK,
                   response_model=ArticleSchemaReponse,
                   response_description="Get article by id"
                   )
async def get_article_by_id(article_id: UUID):
    """get article by id"""
    article_controller = GetArticleByIdController()
    article = await article_controller.handle(Request(params=[article_id]))
    return article[0]
