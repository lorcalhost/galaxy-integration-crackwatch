import sys
import requests
import json
import logging
from pathlib import Path
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType

with open(Path(__file__).parent / 'manifest.json', 'r') as f:
    __version__ = json.load(f)['version']

GIST_URL = 'https://gist.githubusercontent.com/lorcalhost/6eae417c09ebe0035d14f767569afd24/raw/crackwatch-games-list.json'


class CrackWatchPlugin(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.Test,  # choose platform from available list
            __version__,
            reader,
            writer,
            token
        )
        
    # required
    async def authenticate(self, stored_credentials=None):
        logging.info("authenticate called")
        user_data = {}
        user_data['username'] = 'Crackwatcher'       
        self.store_credentials(user_data)
        return Authentication('Crackwatch', user_data['username'])

    async def pass_login_credentials(self, step, credentials, cookies):
        logging.info("pass_login_credentials called")
        user_data = {}
        user_data['username'] = 'Crackwatcher'       
        self.store_credentials(user_data)
        return Authentication('Crackwatch', user_data['username'])

    # required
    async def get_owned_games(self):
        logging.info("get_owned_games called")
        r = requests.get(GIST_URL)
        data = json.loads(r.text)
        games_list = list()
        for entry in data:
            x = Game(
                game_id = entry["slug"],
                game_title = entry["title"],
                license_info = LicenseInfo(LicenseType.SinglePurchase),
                dlcs = []
            )
            games_list.append(x)
        return games_list

    async def check_for_new_games(self):
        logging.info("check_for_new_games called")
        games = await self.get_owned_games()
        for game in games:
            if game not in self.owned_games_cache:
                self.owned_games_cache.append(game)
                self.add_game(game)


def main():
    create_and_run_plugin(CrackWatchPlugin, sys.argv)


# run plugin event loop
if __name__ == "__main__":
    main()
