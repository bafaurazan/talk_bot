""""""

import psutil
import os


def ps_manager():
    ps_list = []

    for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                process_info = proc.info

                if process_info['exe']:
                    ps_list.append(process_info['exe'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    return ps_list
