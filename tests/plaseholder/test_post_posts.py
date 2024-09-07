import json
import allure
from framework.clients.placeholder_client import post_posts
from framework.models.post_posts_model import PostPostsModel

allure_title = "Передаём инфу"
allure_method = "POST /posts"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestPostPosts:

    @allure.id(3)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Добавляем юзера")
    @allure.description(f"{allure_method}. Добавляем юзера")
    def test_post_posts(self):
        with allure.step("Подготавливаем тело запроса"):
            payload = json.dumps({
                "userId": "52",
                "title": "Хорошего дня проверяющему))"
            })
        with allure.step(f"Шаг 1: Отправляем Post запрос для создания нового юзера"):
            response = post_posts(data=payload)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 201"):
            assert response.status_code == 201, f"Статус код не равен 201, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем модель ответа, а так же проверяем, что userId = 52"):
            response_model = PostPostsModel(**response.json())
            assert type(response_model.id) == int, "id нового юзера не int"



