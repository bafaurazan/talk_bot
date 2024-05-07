"""Functions for argument_parser_app_run.py"""

import os
import subprocess
from pathlib import Path
from ..platform_dependency_app_run import (
    my_platform,
    shell_execute_type,
    import_pexpect_wexpect,
)

shell_execute_type = shell_execute_type()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def test_subprocessing():
    """Testing subprocessing capabilities"""
    os.chdir(BASE_DIR / "api")
    result = subprocess.run(
        ["poetry", "env", "info"],
        shell=shell_execute_type,
        check=False,
        stdout=subprocess.PIPE,
    )
    output = result.stdout.decode("utf-8")
    assert "Path:" in output, "Poetry environment missing path information"


def test_pexpect_wexpect():
    """Testing pexpect and expect capabilities"""
    platform_pexpect = import_pexpect_wexpect()
    if my_platform == "Windows":
        child = platform_pexpect.spawn("cmd")
        child.expect(">")
        child.sendline("cd api/ && poetry env info")
        child.expect(">")
        print(child.before)
        child.sendline("exit")
        child.close()
    else:
        print("brak testu dla pexpect")
