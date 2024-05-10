#!/usr/bin/env python3

"""Graphical User Interface management"""

import flet as ft
import pyautogui as pag
import ps_manager as ps_m


def main(page: ft.Page):
    page.title = "talk_bot"

    dlg = ft.AlertDialog(
        title=ft.Text("WORKS"), on_dismiss=lambda e: print("Dialog dismissed!")
    )


    def button_clicked(e):
        ps_m.add_button()
        page.dialog = dlg
        dlg.open = True
        page.update()


    page.window_height = pag.size()[1]
    page.window_width = pag.size()[0] // 8

    page.window_top = 0
    page.window_left = pag.size()[0] - pag.size()[0] // 8

    page.window_bgcolor = "transparent"
    page.window_frameless = True
    page.window_focused = True


    buttons = ft.Row(
        [
            ft.Column(
                [
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ADD_CIRCLE,
                                    icon_color="green",
                                    icon_size=50,
                                    tooltip="Add to db",
                                    on_click=button_clicked
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.Icon(
                                    name=ft.icons.PLAYLIST_ADD_CIRCLE,
                                    color="blue",
                                    size=50,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.Icon(
                                    name=ft.icons.BUILD_CIRCLE, color="gray", size=50
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.window_visible = True

    page.add(buttons)
    page.update()


ft.app(target=main, view=ft.FLET_APP_HIDDEN)
