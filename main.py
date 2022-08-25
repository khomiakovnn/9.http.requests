import requests


def smart_compare(url, superheroes):
    """Collect and compare superheroes intelligence statistics from url"""

    response = requests.get(url)
    if response.status_code == 200:
        print("Request complete")
    else:
        print("bad request")
    smart_dict = {}
    for item in response.json():
        if item["name"] in superheroes:
            smart_dict[item["name"]] = item["powerstats"]["intelligence"]
    return f'Самый умный - {max(smart_dict)}'


def upload(file_path, path_upload, token):
    """Upload file from path to Yandex.Disk"""

    # Receive link for upload
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {"path": path_upload, "overwrite": "true"}
    href = requests.get(url, headers=headers, params=params).json()['href']

    # Upload file from file path
    with open(file_path, 'rb') as file:
        response = requests.put(href, data=file)
    # response = requests.put(href, data=open(file_path, "rb")) # такой вариант загрузки файла был в лекции (без close)
    response.raise_for_status()
    if response.status_code == 201:
        print("Success")


def run():
    """Main function"""
    # Задача №1
    # url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    # superheroes = ["Hulk", "Captain America", "Thanos"]
    # print(smart_compare(url, superheroes))
    # -----------------------------------------------------------------------------

    # Задача №2
    file_path = "files/avatar.jpeg"
    path_upload = "/Netology/avatar.jpeg"
    token = 'XXX'  # Здесь был токен
    upload(file_path, path_upload, token)
    # -----------------------------------------------------------------------------

    # Задача №3

    # -----------------------------------------------------------------------------


if __name__ == "__main__":
    run()
