import requests
import logging

base_url = "https://jsonplaceholder.typicode.com"


def get_posts(**kwargs):
    logging.info("Дёргаем ручку GET для получения информации о пользователе")
    api_handler = f"{base_url}/posts"
    return requests.get(api_handler, **kwargs)


def post_posts(**kwargs):
    logging.info("Дёргаем ручку POST для добавлении инфы о пользователе")
    api_handler = f"{base_url}/posts"
    return requests.post(api_handler, **kwargs)


def put_posts(**kwargs):
    logging.info("Дёргаем ручку PUT для обновлении информации о пользователе")
    api_handler = f"{base_url}/posts/1"
    return requests.put(api_handler, **kwargs)


def delete_posts(**kwargs):
    logging.info("Дёргаем ручку DELETE что бы удалить информацию о пользователе")
    api_handler = f"{base_url}/posts/1"
    return requests.delete(api_handler, **kwargs)
