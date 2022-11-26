# pylint: disable=line-too-long
URL_REGEX = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

article_validator_schema: dict[str, dict] = {
    "title": {
        "type": "string",
        "required": True,
        "min": 6,
    },
    "summary": {
        "type": "string",
        "required": True,
        "min": 20,
    },
    "news_site": {
        "type": "string",
        "required": True,
        "min": 3,
    },
    "featured": {
        "type": "boolean"
    },
    "url": {
        "type": "string",
        "required": True,
        "regex": URL_REGEX,
    },
    "image_url": {
        "type": "string",
        "required": True,
        "regex": URL_REGEX,
    },
}
