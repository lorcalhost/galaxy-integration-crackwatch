# GOG Galaxy integration for crackwatch.com
This plugin allows you to list as owned all the AAA titles marked as cracked on [crackwatch.com](https://crackwatch.com/) in your GOG Galaxy 2.0 launcher.   
  
>*Crackwatch currently lists a total of **17796** cracked games of which **1189** are AAA.*  
>*Due to there being so many listed cracked games, the GOG client would continuously crash when trying to import over 17k games, therefore I decided to focus this project on AAA titles only*

## Installation
1. Download [latest release](https://github.com/lorcalhost/galaxy-integration-crackwatch/releases/latest) of the plugin.
2. Navigate to the GOG Galaxy plugins folder:
	- Windows: `%LOCALAPPDATA%\GOG.com\Galaxy\plugins\installed\<my-plugin-name>`
	- MacOS: `${HOME}/Library/Application Support/GOG.com/Galaxy/plugins/installed/<my-plugin-name>`
3. Unpack the downloaded file inside this folder.
4. Restart GOG Galaxy Client.

## Issue reporting
Along with you detailed problem description, you may need to attach plugin log files located at:
- Windows: `%programdata%\GOG.com\Galaxy\logs`
- MacOS: `/Users/Shared/GOG.com/Galaxy/Logs`

For example:
`C:\ProgramData\GOG.com\Galaxy\logs\crackwatch-6eae417c-09eb-e003-5d14-f767569afd24.log`

## Development

1. Create and activate virtual environment
2. Install dependencies

        pip install -r requirements/dev.txt

3. Install to your local GOG galaxy plugins folder
 
        inv install


## Disclaimer
- I am in no way associated with [crackwatch.com](https://crackwatch.com/). This project was made possible thanks to [their api](https://crackwatch.com/api)
- I do not support piracy and I do not encourage it, this is a purely educational project aimed at keeping track of what's happening in the game cracking scene.
- Please support game developers and do not pirate games; other than being illegal in many countries, game piracy also hurts the gaming industry.
