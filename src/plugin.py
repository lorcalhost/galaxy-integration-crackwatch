import sys
import requests
import json
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
            __version__,  # version
            reader,
            writer,
            token
        )

    # implement methods

    # required
    async def authenticate(self, stored_credentials=None):
        return Authentication('Crackwatch', 'Crackwatch')

    # required
    async def get_owned_games(self):
        r = requests.get(GIST_URL)
        data = json.loads(r.text)
        games_list = list()
        for entry in data:
            print(f'{entry["slug"]} {entry["title"]}')
            x = Game(
                game_id = entry["slug"],
                game_title = entry["title"],
                license_info = LicenseInfo(LicenseType.SinglePurchase),
                dlcs = []
            )
            games_list.append(x)
        return games_list


def main():
    create_and_run_plugin(CrackWatchPlugin, sys.argv)


# run plugin event loop
if __name__ == "__main__":
    main()
