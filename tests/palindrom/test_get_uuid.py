import allure
import pytest
from framework.clients.palindrom_client import get_palindrom
from framework.models.get_uuid_model import GetUuidModel

allure_title = "Получаем информацию о слове"
allure_method = "GET /uuid"


@allure.label("owner", "Egorov Kirill")
@allure.label("layer", "API")
@allure.label("Method", allure_method)
class TestGetUuid:

    @allure.id(1)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Получаем информацию")
    @allure.description(f"{allure_method}. Получаем информацию")
    def test_get_uuid(self, new_word_palindrom):
        with allure.step(f"Шаг 1: Отправляем GET запрос для получения информации о слово по uuid"):
            response = get_palindrom(uuid=new_word_palindrom.id)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 200"):
            assert response.status_code == 200, f"Статус код не равен 200, а равен {response.status_code}"
        with allure.step("Шаг 3: Провеярем модель ответа, и проверяем, что слово по uuid является палиндромом"):
            response_model = GetUuidModel(**response.json())
            assert response_model.result.lower() == response_model.result.lower()[
                                                    ::-1], "Слово которое создалось не является палиндромом"

    """Так же можно делать проверки с самим юрлом"""

    @allure.id(4)  # в дальнейшем прицепить id allurы
    @allure.label("priority", "Критический")
    @allure.title(f"{allure_title} Получаем информацию")
    @allure.description(f"{allure_method}. Получаем информацию")
    @pytest.mark.parametrize(["negative_url", "test_description"],
                             [(" ", "С пробелами в конце юрла"),
                              ("00000-0000000-00000", "Рандомные числа в uuid")])  # сценариев можно придумать много
    def test_get_uuid_negative(self, negative_url, test_description):
        with allure.step(
                f"Шаг 1: Отправляем GET запрос для получения информации о слово c негативными uuid {test_description}"):
            response = get_palindrom(uuid=negative_url)
        with allure.step("Шаг 2: Проверяем, что статус код ответ 400"):
            assert response.status_code == 400, f"Статус код не равен 400, а равен {response.status_code}"

