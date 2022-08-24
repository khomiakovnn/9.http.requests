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


def run():
    """Main function"""
    # Задача №1
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    superheroes = ["Hulk", "Captain America", "Thanos"]
    print(smart_compare(url, superheroes))
    # -----------------------------------------------------------------------------

    # Задача №2
    # url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    # superheroes = ["Hulk", "Captain America", "Thanos"]
    # print(smart_compare(url, superheroes))
    # -----------------------------------------------------------------------------

    # Задача №3
    # url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    # superheroes = ["Hulk", "Captain America", "Thanos"]
    # print(smart_compare(url, superheroes))
    # -----------------------------------------------------------------------------


if __name__ == "__main__":
    run()
