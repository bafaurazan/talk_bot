"""Argument parser for app_run"""

import argparse
import threading
from app_run_config.functions_app_run import (
    api_preparing,
    talk_bot_preparing,
    api_run,
    talk_bot_run,
)

from app_run_config.test.test_app_run import (
    test_subprocessing,
)


def argument_parser_for_app_run():
    """
    There are defined args to use by app_run.py
    based on functions in app_run_config/functions_app_run.py
    """
    parser = argparse.ArgumentParser(description="Project runner")
    parser.add_argument(
        "--install", action="store_true", help="install project requirements"
    )
    parser.add_argument("--test", action="store_true", help="test project")

    args = parser.parse_args()

    if args.install:
        threading.Thread(target=api_preparing).start()
        threading.Thread(target=talk_bot_preparing).start()
    elif args.test:
        threading.Thread(target=test_subprocessing).start()
    else:
        threading.Thread(target=api_run).start()
        threading.Thread(target=talk_bot_run).start()
