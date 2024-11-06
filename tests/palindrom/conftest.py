import pytest
import allure
import json
from framework.clients.palindrom_client import post_polindrom
from framework.models.post_posts_model import PostPalindromModel


@pytest.fixture(scope="function")
def new_word_palindrom():
    with allure.step("Подготавливаем тело запроса с условием, что palindrom = True"):
        payload = json.dumps({
            "palindrom": True
        })
    with allure.step(f"Шаг 1: Отправляем Post запрос для создания слова"):
        response = post_polindrom(data=payload)
    with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
        assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
    with allure.step("Шаг 3: Провеярем модель ответа, а так же проверяем, что созданное слово палиндром"):
        response_model = PostPalindromModel(**response.json())
        assert response_model.result.lower() == response_model.result.lower()[
                                                ::-1], "Слово которое создалось не является палиндромом"
        yield response_model
