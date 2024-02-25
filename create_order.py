import config
import requests

def get_docs():
    return requests.get(config.URL_SERVICE + config.DOC_PATH)

     #Создание заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.ORDER_PATH, #подставляем полный url
                    json=body) #тело запроса

     #Заказ по треку
def get_order_by_track_number(track_numder):
    response = requests.get(config.URL_SERVICE + config.ORDER_TRACK_DATA_PATH + track_numder)
    return response.status_code
