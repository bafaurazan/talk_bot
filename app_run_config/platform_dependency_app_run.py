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
