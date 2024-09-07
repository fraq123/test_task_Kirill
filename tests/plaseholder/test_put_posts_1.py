import json
import allure
import pytest
from framework.clients.placeholder_client import put_posts
from framework.models.put_posts_1_model import PutPosts1Model

allure_title = "Обновляем инфу"
allure_method = "PUT /posts/1"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestPutPosts1:

    @allure.id(4)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Обновляем юзера")
    @allure.description(f"{allure_method}. Обновляем юзера")
    @pytest.mark.parametrize(["body", "title", "test_description"],
                             [("Обновялем", "", "field title is empty"), ("", "Исправляем", "field body is empty")])
    def test_put_posts_1(self, body, title, test_description):
        with allure.step("Подготавливаем тело запроса"):
            payload = json.dumps({
                "userId": "1",
                "body": body,
                "title": title
            })
        with allure.step(f"Шаг 1: Отправляем PUT запрос для изменения данных юзера"):
            response = put_posts(data=payload)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
            assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем модель ответа, а так же проверяем, что userId = 52"):
            PutPosts1Model(**response.json())

