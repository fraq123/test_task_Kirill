import json
import allure
from framework.clients.placeholder_client import delete_posts

allure_title = "Удаляем инфу"
allure_method = "DELETE /posts/1"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestDeletePosts1:

    @allure.id(1)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Удаляем юзера")
    @allure.description(f"{allure_method}. Удаляем юзера")
    def test_delete_posts_1(self):
        with allure.step("Подготавливаем тело запроса"):
            payload = json.dumps({
                "userId": "1"
            })
        with allure.step(f"Шаг 1: Отправляем PUT запрос для изменения данных юзера"):
            response = delete_posts(data=payload)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
            assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем, что ответ пришел пустой"):
            assert response.json() == {}, "Ответ пришел не пустой"
        #  если бы полноценный проект был, то добавил бы проверку или в БД, на проверку удалился ли пользвоатель
        #  или добавил проверку на какую нить GET ручку по ид пользователя
