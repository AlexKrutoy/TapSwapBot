[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)

Thanks for idea:
[<img src="https://img.shields.io/badge/Telegram-%40shamhi-orange">](https://t.me/sho6ot)


![img1](.github/images/demo.png)

> 🇷🇺 README на русском доступен [здесь](README.md)

## Functionality
| Functional                                                     | Supported |
|----------------------------------------------------------------|:---------:|
| Multithreading                                                 |     ✅     |
| Binding a proxy to a session                                   |     ✅     |
| Auto-purchase of items if you have coins (tap, energy, charge) |     ✅     |
| Random sleep time between clicks                               |     ✅     |
| Random number of clicks per request                            |     ✅     |
| Support tdata / pyrogram .session / telethon .session          |     ✅     |

## [Settings](https://github.com/shamhi/TapSwapBot/blob/main/.env-example)
| Настройка                | Описание                                                                               |
|--------------------------|----------------------------------------------------------------------------------------|
| **API_ID / API_HASH**    | Platform data from which to launch a Telegram session (stock - Android)                |
| **MIN_AVAILABLE_ENERGY** | Minimum amount of available energy, upon reaching which                                |
|                          | there will be a delay (eg [10, 100])                                                   |
| **SLEEP_BY_MIN_ENERGY**  | Delay when reaching minimum energy in seconds (eg [40, 200])                           |
| **ADD_TAPS_ON_TURBO**    | How many taps will be added when turbo is activated (eg 2500)                          |
| **AUTO_UPGRADE_TAP**     | Should I improve the tap (True / False)                                                |
| **MAX_TAP_LEVEL**        | Maximum level of tap pumping (up to 20)                                                |
| **AUTO_UPGRADE_ENERGY**  | Should I improve the energy (True / False)                                             |
| **MAX_ENERGY_LEVEL**     | Maximum level of energy pumping (up to 20)                                             |
| **AUTO_UPGRADE_CHARGE**  | Should I improve the charge (True / False)                                             |
| **MAX_CHARGE_LEVEL**     | Maximum level of charge pumping (up to 5)                                              |
| **APPLY_DAILY_ENERGY**   | Whether to use the daily free energy boost (True / False)                              |
| **APPLY_DAILY_TURBO**    | Whether to use the daily free turbo boost (True / False)                               |
| **RANDOM_CLICKS_COUNT**  | Random number of taps (eg [50,200])                                                    |
| **SLEEP_BETWEEN_TAP**    | Random delay between taps in seconds (eg [10,25])                                      |
| **USE_PROXY_FROM_FILE**  | Whether to use proxy from the `bot/config/proxies.txt` file (True / False)             |

## Quick Start 📚
1. To install libraries on Windows click on `INSTALL.bat`.
2. To start the bot use `START.bat` (or in console: `python main.py`).

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) version 3.10 or 3.11

## Obtaining API Keys
1. Go to [my.telegram.org](https://my.telegram.org) and log in using your phone number.
2. Select **"API development tools"** and fill out the form to register a new application.
3. Note down the `API_ID` and `API_HASH` in `.env` file provided after registering your application.

## Installation
You can download [**Repository**](https://github.com/AlexKrutoy/TapSwapBot) by cloning it to your system and installing the necessary dependencies:
```shell
~ >>> git clone https://github.com/AlexKrutoy/TapSwapBot.git
~ >>> cd TapSwapBot

# If you are using Telethon sessions, then clone the "converter" branch
~ >>> git clone https://github.com/shamhi/TapSwapBot.git -b converter
~ >>> cd TapSwapBot

#Linux
~/TapSwapBot >>> python3 -m venv venv
~/TapSwapBot >>> source venv/bin/activate
~/TapSwapBot >>> pip3 install -r requirements.txt
~/TapSwapBot >>> cp .env-example .env
~/TapSwapBot >>> nano .env # Here you must specify your API_ID and API_HASH , the rest is taken by default
~/TapSwapBot >>> python3 main.py

#Windows
~/TapSwapBot >>> python -m venv venv
~/TapSwapBot >>> venv\Scripts\activate
~/TapSwapBot >>> pip install -r requirements.txt
~/TapSwapBot >>> copy .env-example .env
~/TapSwapBot >>> # Specify your API_ID and API_HASH, the rest is taken by default
~/TapSwapBot >>> python main.py
```

Also for quick launch you can use arguments, for example:
```shell
~/TapSwapBot >>> python3 main.py --action (1/2)
# Or
~/TapSwapBot >>> python3 main.py -a (1/2)

#1 - Run clicker
#2 - Create session
```
