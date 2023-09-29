# Федор Идоленкв 8а когорта, Финальный прект Инженер по тестированию плюс
import to_requests

def test_get_order():
    track_nt = to_requests.track_order().json()['track']
    assert to_requests.get_order(track_nt).status_code == 200

# подробное описание в README