#!/usr/bin/env python3

""""""

import psutil
import os


def add_button():
    ps_list = []

    for proc in psutil.process_iter(["name", "exe"]):
        if "" in proc.info["name"]:
            ps_list.append((proc.info["exe"]))

    with open(r'demofile.txt', 'w') as fp:
        for item in ps_list:
            fp.write("%s\n" % item)

    # page.update()
    # return ps_list
