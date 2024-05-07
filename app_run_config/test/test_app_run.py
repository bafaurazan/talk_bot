"""Functions for argument_parser_app_run.py"""

import os
import subprocess
from pathlib import Path
from ..platform_dependency_app_run import shell_execute_type

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def test_subprocessing():
    """Crucial preparations for the API and Django operations"""
    os.chdir(BASE_DIR / "api")
    result = subprocess.run(
        ["poetry", "env", "info"],
        shell=shell_execute_type,
        check=False,
        stdout=subprocess.PIPE,
    )
    output = result.stdout.decode("utf-8")
    assert "Path:" in output, "Poetry environment info missing path information"
