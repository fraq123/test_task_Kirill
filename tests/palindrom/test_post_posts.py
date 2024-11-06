import json
import allure
from framework.clients.palindrom_client import post_palindrom
from framework.models.post_posts_model import PostPalindromModel

allure_title = "Создаём слово"
allure_method = "POST /posts"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestPostPosts:

    @allure.id(2)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Добавляем слово")
    @allure.description(f"{allure_method}. Добавляем слово")
    def test_post_posts_true(self):
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
            assert response_model.result.lower() == response_model.result.lower()[::-1], "Слово которое создалось не является палиндромом"

    @allure.id(3)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Добавляем слово")
    @allure.description(f"{allure_method}. Добавляем слово")
    def test_post_posts_false(self):
        with allure.step("Подготавливаем тело запроса с условием, что palindrom = False"):
            payload = json.dumps({
                "palindrom": False
            })
        with allure.step(f"Шаг 1: Отправляем Post запрос для создания слова"):
            response = post_polindrom(data=payload)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
            assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем модель ответа, а так же проверяем, что созданное слово не является палиндромом"):
            response_model = PostPalindromModel(**response.json())
            assert response_model.result.lower() != response_model.result.lower()[
                                                    ::-1], "Слово которое создалось является палиндромом"



