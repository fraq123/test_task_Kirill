import requests
import logging

base_url = "base_url"  # поменять на базовый url


def post_palindrom(**kwargs):
    logging.info("Дёргаем ручку POST для создания слова")
    api_handler = f"{base_url}/posts"
    return requests.post(api_handler, **kwargs)


def get_palindrom(uuid: str):
    logging.info("Дёргаем ручку POST для проверки слова по uuid")
    api_handler = f"{base_url}/{uuid}"
    return requests.get(api_handler)
