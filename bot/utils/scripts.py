import asyncio
from typing import Union

from pyrogram import Client
from pyrogram.types import Message

from bot.utils.emojis import num, StaticEmoji
from bs4 import BeautifulSoup

import pathlib
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


def get_command_args(
        message: Union[Message, str],
        command: Union[str, list[str]] = None,
        prefixes: str = "/",
) -> str:
    if isinstance(message, str):
        return message.split(f"{prefixes}{command}", maxsplit=1)[-1].strip()
    if isinstance(command, str):
        args = message.text.split(f"{prefixes}{command}", maxsplit=1)[-1].strip()
        return args
    elif isinstance(command, list):
        for cmd in command:
            args = message.text.split(f"{prefixes}{cmd}", maxsplit=1)[-1]
            if args != message.text:
                return args.strip()
    return ""


def with_args(text: str):
    def decorator(func):
        async def wrapped(client: Client, message: Message):
            if message.text and len(message.text.split()) == 1:
                await message.edit(f"<emoji id=5210952531676504517>❌</emoji>{text}")
            else:
                return await func(client, message)

        return wrapped

    return decorator


def get_help_text():
    return f"""<b>
{StaticEmoji.FLAG} [Demo version]

{num(1)} /help - Displays all available commands
{num(2)} /tap [on|start, off|stop] - Starts or stops the tapper

</b>"""



async def stop_tasks(client: Client = None) -> None:
    if client:
        all_tasks = asyncio.all_tasks(loop=client.loop)
    else:
        loop = asyncio.get_event_loop()
        all_tasks = asyncio.all_tasks(loop=loop)

    clicker_tasks = [task for task in all_tasks
                     if isinstance(task, asyncio.Task) and task._coro.__name__ == 'run_tapper']

    for task in clicker_tasks:
        try:
            task.cancel()
        except:
            ...

def escape_html(text: str) -> str:
    return text.replace('<', '\\<').replace('>', '\\>')

def extract_chq(chq: str) -> int:
    if not pathlib.Path("webdriver").exists():
        pathlib.Path("webdriver").mkdir(parents=True)
        webdriver_path = pathlib.Path(ChromeDriverManager().install())
        shutil.move(webdriver_path, f"webdriver/{webdriver_path.name}")
    else:
        webdriver_path = next(pathlib.Path("webdriver").iterdir()).as_posix()

    chq_length = len(chq)

    bytes_array = bytearray(chq_length // 2)
    xor_key = 157

    for i in range(0, chq_length, 2):
        bytes_array[i // 2] = int(chq[i:i + 2], 16)

    xor_bytes = bytearray(t ^ xor_key for t in bytes_array)
    decoded_xor = xor_bytes.decode('utf-8')

    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(webdriver_path), options=options)

    driver.execute_script("""
        var chrStub = document.createElement("div");
        chrStub.id = "_chr_";
        document.body.appendChild(chrStub);
    """)

    fixed_xor = repr(decoded_xor).replace("", "\\")

    k = driver.execute_script(f"""
        try {{
            return eval({fixed_xor[1:-1]});
        }} catch (e) {{
            return e;
        }}
    """)

    driver.quit()

    return k
