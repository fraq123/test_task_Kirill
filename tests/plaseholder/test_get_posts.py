import allure
import pytest
from framework.clients.placeholder_client import get_posts
from framework.models.get_posts_model import GetPostsModel

allure_title = "Получаем инфу"
allure_method = "GET /posts"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestGetPosts:

    @allure.id(2)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Получаем информацию")
    @allure.description(f"{allure_method}. Получаем информацию")
    #  не особо понял про какие параметры имеется ввиду в задании, решил использовать просто который придумал и закинул в параметризацию
    @pytest.mark.parametrize(["user_id", "test_description"],
                             [("userId=1", "Use parameters userId=1"), ("userId=3", "Use parameters userId=3")])
    def test_get_posts(self, user_id, test_description):
        with allure.step(f"Шаг 1: Отправляем GET запрос для получения информации с параметрами {test_description}"):
            response = get_posts(params=user_id)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
            assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем модель ответа"):
            response_model = GetPostsModel.parse_obj(response.json())
            # так же можно добавить проверки какие то определённые, уже доставая поля из шага 3, привер:
            assert type(response_model.root[
                            0].id) == int, f"Поле id не является int, а является {type(response_model.root[0].id)}"
