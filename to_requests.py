import config
import data
import requests


def track_order():
    j_data_order=data.JSON_ORDER.copy()
    order_create_response = requests.post(config.URL_SERVICE + config.ORDER_PATH,json=j_data_order, headers=data.headers)
    # print (order_create_response.status_code)
    return order_create_response

def get_order(track_num):
    track_n={'t':track_num}
    get_order_responce = requests.get(config.URL_SERVICE + config.GET_ORDER_PATH, params = track_n, headers=data.headers)
    # print(get_order_responce.status_code)
    # print(get_order_responce.json())
    return get_order_responce
# подробное описание в README