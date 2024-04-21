import allure
from faker import Faker


@allure.step('Генерация данных для нового курьера')
def courier_data_generation():
    fake = Faker()
    data = {
        "login": fake.user_name(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return data
