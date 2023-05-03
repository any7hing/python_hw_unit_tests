import requests
token = "   "
headers = {'Content-Type': 'application/json', 'Authorization': token}


def create_folder_ya_api(name_folder: str):
    URL = f"https://cloud-api.yandex.net/v1/disk/resources?path={name_folder}"
    responce = requests.put(URL, headers=headers)
    return responce


def check_folder_yandex(name_folder: str):
    URL = f"https://cloud-api.yandex.net/v1/disk/resources?path={name_folder}"
    responce = requests.get(URL, headers=headers)
    return responce.status_code


if __name__ == '__main__':
    create_folder_ya_api('test4')
    check_folder_yandex('test4')
