"""Main file to run project"""

import argparse
import threading
import subprocess
from pathlib import Path
from platform_dependency_main import comand_shell_execute_type

platform_dependency = comand_shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent


def api_preparing():
    """Crucial preparations for the API and Django operations"""
    subprocess.run(
        ["cd", str(BASE_DIR / "api"), "&&",
         "poetry", "install", "&&",
         "poetry", "run", "python", "manage.py", "makemigrations", "&&",
         "poetry", "run", "python", "manage.py", "migrate"
         ], shell=platform_dependency,
        check=True,
    )


def talk_bot_preparing():
    """Crucial preparations for talk_bot operation"""
    subprocess.run(
        ["cd", str(BASE_DIR / "my_bot/bot_config"), "&&",
         "poetry", "install"],
        shell=platform_dependency,
        check=True
    )


def api_run():
    """Running django server"""
    subprocess.run(
        ["cd", str(BASE_DIR / "api"), "&&",
         "poetry", "run", "python", "manage.py", "runserver"],
        shell=platform_dependency,
        check=True,
    )


def talk_bot_run():
    """Running talk_bot"""
    subprocess.run(
        ["cd", str(BASE_DIR / "my_bot/bot_config"), "&&",
         "poetry", "run", "python", "bot.py"],
        shell=platform_dependency,
        check=True
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific app")
    parser.add_argument("--install", action="store_true", help="App to run")
    args = parser.parse_args()

    if args.install:
        t1 = threading.Thread(target=api_preparing)
        t1.start()
        t2 = threading.Thread(target=talk_bot_preparing)
        t2.start()

    else:
        t1 = threading.Thread(target=api_run)
        t1.start()
        t2 = threading.Thread(target=talk_bot_run)
        t2.start()
