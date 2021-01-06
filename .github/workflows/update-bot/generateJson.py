import json
import requests
import time

MAIN_URL = 'https://api.crackwatch.com/api/games'


if __name__ == '__main__':
    t = time.time()
    games_list = list()
    page = 0
    while True:
        print(f'Page {page}')
        r = requests.get(MAIN_URL, params={
                         'page': page, 'sort_by': 'crack_date', 'is_cracked': 'true', 'is_aaa': 'true'})
        data = json.loads(r.text)
        if not data:
            break
        for game in data:
            del game['isAAA']
            del game['NFOsCount']
            del game['commentsCount']
            del game['followersCount']
            del game['protections']
            del game['versions']
            del game['groups']
            del game['updatedAt']
            del game['releaseDate']
            del game['crackDate']
            games_list.append(game)
        page += 1
        time.sleep(1)

    with open('crackwatch-games-list.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(games_list, indent=4, ensure_ascii=False))
    print(f'Completed, elapsed time: {round(time.time() - t, 2)} seconds')
