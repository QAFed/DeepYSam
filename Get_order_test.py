# Федор Идоленкв 8а когорта, Финальный прект Инженер по тестированию плюс
import to_requests

def test_get_order():
    assert to_requests.get_order().status_code == 200
# подробное описание в README