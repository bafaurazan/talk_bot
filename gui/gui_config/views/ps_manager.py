""""""

import psutil
import os


def ps_manager():
    ps_list = []

    for proc in psutil.process_iter(["name", "exe"]):
        if "" in proc.info["name"]:
            ps_list.append((proc.info["exe"]))

    with open(r'demofile.txt', 'w') as fp:
        for item in ps_list:
            fp.write("%s\n" % item)

    return ps_list
