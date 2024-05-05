"""Functions for argument_parser_app_run.py"""

import subprocess
from pathlib import Path
from ..platform_dependency_app_run import shell_execute_type

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def test_subprocessing():
    """Crucial preparations for the API and Django operations"""
    subprocess.run(
        [
            "cd",
            str(BASE_DIR / "api"),
            "&&",
            "poetry",
            "install",
        ],
        shell=shell_execute_type,
        check=True,
    )
