""""""

import flet as ft

def IndexView(page, ft=ft):
    def add_command_button(e):
       # page.go("/add_command")
       pass

    def add_ps_button(e):
       page.go("/add_ps")


    content = ft.Row(
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
                                    on_click=add_command_button
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.PLAYLIST_ADD_CIRCLE,
                                    icon_color="blue",
                                    icon_size=50,
                                    tooltip="TODO",
                                    on_click=add_ps_button
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.BUILD_CIRCLE,
                                    icon_color="gray",
                                    icon_size=50,
                                    tooltip="TODO"
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

    return content
