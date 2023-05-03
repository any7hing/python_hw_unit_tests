from main import filter_logs, unique_id, max_stats
from yandex_api import *


class Testmain:
    def test_geo_logs(self):
        res = filter_logs()
        for item in res:
            for val in item.values():
                assert "Россия" in val

    def test_unique_id(self):
        res = unique_id()
        assert len(res) == len(set(res))
        for item in res:
            assert type(item) is int

    def test_max_stats(self):
        res = max_stats()
        assert type(res) is int
        assert res == 120

    def test_ya_api_folder(self):
        res = create_folder_ya_api('test4')
        responce_code = check_folder_yandex('test4')
        assert res.status_code == 201
        assert responce_code == 200, "проверка что папка существует"
        assert res.status_code != 409, "Папка с таким именем уже существует"
        assert res.status_code != 401, "Ошибка авторизации"
