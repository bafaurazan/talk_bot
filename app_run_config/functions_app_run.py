"""Functions for argument_parser_app_run.py"""

import subprocess
from pathlib import Path
from .platform_dependency_app_run import shell_execute_type

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent


def api_preparing():
    """Crucial preparations for the API and Django operations"""
    subprocess.run(
        [
            "cd",
            str(BASE_DIR / "api"),
            "&&",
            "poetry",
            "install",
            "&&",
            "poetry",
            "run",
            "python",
            "manage.py",
            "makemigrations",
            "&&",
            "poetry",
            "run",
            "python",
            "manage.py",
            "migrate",
        ],
        shell=shell_execute_type,
        check=True,
    )


def talk_bot_preparing():
    """Crucial preparations for talk_bot operation"""
    subprocess.run(
        ["cd", str(BASE_DIR / "my_bot/bot_config"), "&&", "poetry", "install"],
        shell=shell_execute_type,
        check=True,
    )


def api_run():
    """Running django server"""
    subprocess.run(
        [
            "cd",
            str(BASE_DIR / "api"),
            "&&",
            "poetry",
            "run",
            "python",
            "manage.py",
            "runserver",
        ],
        shell=shell_execute_type,
        check=True,
    )


def talk_bot_run():
    """Running talk_bot"""
    subprocess.run(
        [
            "cd",
            str(BASE_DIR / "my_bot/bot_config"),
            "&&",
            "poetry",
            "run",
            "python",
            "bot.py",
        ],
        shell=shell_execute_type,
        check=True,
    )
