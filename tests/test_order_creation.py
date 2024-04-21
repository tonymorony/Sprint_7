import allure
import pytest
from data import TestsData as TD
from api.order_api import OrderApi


class TestOrderCreation:
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title('Проверка создания заказа с цветом: {colors}')
    def test_successful_order_creation(self, colors):
        order_api = OrderApi()
        order_data = TD.ORDER_TEST_DATASET
        order_data['color'] = colors
        response = order_api.create_order(order_data)
        assert response.status_code == 201 and "track" in response.json()
