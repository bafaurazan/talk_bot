"""Functions for argument_parser_app_run.py"""

import os
import subprocess
from pathlib import Path
from .platform_dependency_app_run import shell_execute_type

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent


def api_preparing():
    """Crucial preparations for the API and Django operations"""
    os.chdir(BASE_DIR / "api")
    subprocess.run(
        ["poetry", "install"],
        shell=shell_execute_type,
        check=True,
    )
    os.chdir(BASE_DIR / "api")
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "makemigrations"],
        shell=shell_execute_type,
        check=True,
    )
    os.chdir(BASE_DIR / "api")
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "migrate"],
        shell=shell_execute_type,
        check=True,
    )


def talk_bot_preparing():
    """Crucial preparations for talk_bot operation"""
    os.chdir(BASE_DIR / "my_bot")
    subprocess.run(
        ["poetry", "install"],
        shell=shell_execute_type,
        check=True,
    )


def api_run():
    """Running django server"""
    os.chdir(BASE_DIR / "api")
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "runserver"],
        shell=shell_execute_type,
        check=True,
    )


def talk_bot_run():
    """Running talk_bot"""
    os.chdir(BASE_DIR / "my_bot/bot_config")
    subprocess.run(
        ["poetry", "run", "python", "bot.py"],
        shell=shell_execute_type,
        check=True,
    )
