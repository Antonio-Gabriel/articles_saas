import uvicorn

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from bootstrap import *  # pylint: disable=unused-wildcard-import, wildcard-import
from src.presenters.http.routes import article_route

app = FastAPI(redoc_url=False)

app.title = "Articles Saas"
app.description = "An application for register articles"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Start"])
def main():
    """main route"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=dict(
            message="Back-end Challenge 2022 🏅 - Space Flight News"
        )
    )


app.include_router(article_route)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
