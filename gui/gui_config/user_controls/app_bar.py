""""""

import flet as ft

def NavBar(page, ft=ft):
    def on_close(e):
        page.window_destroy()


    NavBar = ft.AppBar(
        leading_width=40,
        # title=ft.Text("talk_bot"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
            ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings')),
            ft.IconButton(ft.icons.CLOSE, on_click=on_close)
        ]
    )

    return NavBar
