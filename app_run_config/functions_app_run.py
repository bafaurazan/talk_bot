"""Functions for argument_parser_app_run.py"""

import os
import subprocess
from pathlib import Path
from .platform_dependency_app_run import shell_execute_type

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent


def api_preparing():
    """Crucial preparations for the API and Django operations"""
    subprocess.run(
        ["poetry", "env", "use", "3.12"],
        cwd=str(BASE_DIR / "api"),
        shell=shell_execute_type,
        check=False,
    )
    subprocess.run(
        ["poetry", "install"],
        cwd=str(BASE_DIR / "api"),
        shell=shell_execute_type,
        check=False,
    )
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "makemigrations"],
        cwd=str(BASE_DIR / "api"),
        shell=shell_execute_type,
        check=False,
    )
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "migrate"],
        cwd=str(BASE_DIR / "api"),
        shell=shell_execute_type,
        check=False,
    )


def talk_bot_preparing():
    """Crucial preparations for talk_bot operation"""
    subprocess.run(
        ["poetry", "env", "use", "3.12"],
        cwd=str(BASE_DIR / "my_bot"),
        shell=shell_execute_type,
        check=False,
    )
    subprocess.run(
        ["poetry", "install"],
        cwd=str(BASE_DIR / "my_bot"),
        shell=shell_execute_type,
        check=False,
    )


def api_run():
    """Running django server"""
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "runserver"],
        cwd=str(BASE_DIR / "api"),
        shell=shell_execute_type,
        check=False,
    )


def talk_bot_run():
    """Running talk_bot"""
    subprocess.run(
        ["poetry", "run", "python", "bot.py"],
        cwd=str(BASE_DIR / "my_bot/bot_config"),
        shell=shell_execute_type,
        check=False,
    )
