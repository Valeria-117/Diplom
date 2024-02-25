# Гусева Валерия, 13-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import create_order


# Выполнение запроса на создание заказа
def create_new_order():
    # тело запроса
    request_body = data.order_body
    # создание заказа
    response_order = create_order.post_new_order(request_body)
    # cохранение номера трэк заказа
    return response_order.json()["track"]

    # Отправка запроса на получения информации о заказе по треку и проверка ответа


def test_get_info_order():
    current_track_number = create_new_order()
    response_status_code = create_order.get_order_by_track_number(str(current_track_number))
    assert response_status_code == 200