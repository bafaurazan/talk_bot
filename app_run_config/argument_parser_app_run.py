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
    test_pexpect_wexpect,
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
        thr_api = threading.Thread(target=api_preparing)
        thr_api.start()
        thr_talk_bot = threading.Thread(target=talk_bot_preparing)
        thr_talk_bot.start()
    elif args.test:
        thr_subbrocessing = threading.Thread(target=test_subprocessing)
        thr_subbrocessing.start()
        thr_pexpect_wexpect = threading.Thread(target=test_pexpect_wexpect)
        thr_pexpect_wexpect.start()
    else:
        thr_api = threading.Thread(target=api_run)
        thr_api.start()
        thr_talk_bot = threading.Thread(target=talk_bot_run)
        thr_talk_bot.start()
