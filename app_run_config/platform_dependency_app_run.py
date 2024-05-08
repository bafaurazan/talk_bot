"""Platform dependency for functions_app_run.py"""

import platform

my_platform = platform.system()


def shell_execute_type():
    """
    In subprocess.run( shell=<False/True> )
    On windows platform must be set to "True"
    On others platform must be set to "False"
    """
    return my_platform == "Windows"


def import_pexpect_wexpect():
    """
    wexpect and pexpect are packages to controll external apps
    wexpect is only viable for windows
    pexpect is viable for others platforms
    """
    if my_platform == "Windows":
        import wexpect

        my_pexpect = wexpect
    else:
        import pexpect

        my_pexpect = pexpect
    return my_pexpect
