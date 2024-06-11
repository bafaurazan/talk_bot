#!/usr/bin/env python3

"""Graphical User Interface management"""

import flet as ft
import pyautogui as pag

from views.FletRouter import Router
from user_controls.app_bar import NavBar

def main(page: ft.Page):
    page.title = "talk_bot"


    page.appbar = NavBar(page, ft)
    myRouter = Router(page, ft)
    page.on_route_change = myRouter.route_change


    # size of the main window
    page.window_height = pag.size()[1]
    page.window_width = pag.size()[0] // 8
    page.window_top = 0
    page.window_left = pag.size()[0] - pag.size()[0] // 8


    # main window settings
    page.window_bgcolor = "transparent"
    page.window_frameless = True
    page.window_focused = True
    page.window_visible = True
    page.theme_mode = "dark"


    # center routes
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER



    page.add(
        myRouter.body
    )
    page.go('/')


ft.app(target=main, view=ft.FLET_APP_HIDDEN, assets_dir="assets")
