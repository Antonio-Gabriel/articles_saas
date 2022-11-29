from rocketry import Rocketry
from rocketry.conds import daily, after_fail, after_success

from ...presenters.controllers.carrie_articles_controller import (
    CarrieArticleController
)

app = Rocketry(execution='async')


@app.task(daily.at('9:00'))
async def carrie_new_articles_into_database():
    """This script will execute every day 9 hour to add new articles in the database"""
    article_controller = CarrieArticleController()
    await article_controller.handle()


@app.task(after_fail(carrie_new_articles_into_database))
async def failed_load_articles_process():
    """run this func if an error occured in the request"""
    print("An error occured, please check the log for more details")


@app.task(after_success(carrie_new_articles_into_database))
async def articled_added_from_database():
    """run this func after carrie all articles from db"""
    print("Articles inserted successfully")


if __name__ == "__main__":
    app.run()
