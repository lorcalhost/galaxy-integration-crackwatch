import json
import requests
import time

MAIN_URL = 'https://api.crackwatch.com/api/games'


if __name__ == '__main__':
    t = time.time()
    games_list = list()
    page = 0
    while True:
        r = requests.get(MAIN_URL, params={
                         'page': page, 'sort_by': 'crack_date', 'is_cracked': 'true', 'is_aaa': 'true'})
        data = json.loads(r.text)
        if not data:
            break
        for game in data:
            x = {
                "slug": game["slug"],
                "title": game["title"]
            }
            games_list.append(x)
        page += 1
        time.sleep(1)

    with open('crackwatch-games-list.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(games_list, indent=4, ensure_ascii=False))
    print(f'Fetched {page} pages, elapsed time: {round(time.time() - t, 2)} seconds')
