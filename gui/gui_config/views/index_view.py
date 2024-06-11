"""Page view route displaying main page of the app"""

import flet as ft
import requests


def get_commands():
    url = 'http://127.0.0.1:8000/api/document/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    else:
        print(f"Failed to retrieve items. Status code: {response.status_code}")


    return data



def IndexView(page, ft=ft):
    """Displays option buttons and routes after clicking on them"""

    def add_command_button(e):
       page.go("/add_command")

    def add_ps_button(e):
       page.go("/add_ps")

    def list_button(e):
        get_commands()
        page.go("/list_commands")


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
                                    tooltip="Add shell command",
                                    on_click=add_command_button
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ),
                    # ft.TextButton(
                    #     width=100,
                    #     content=ft.Row(
                    #         [
                    #             ft.IconButton(
                    #                 icon=ft.icons.PLAYLIST_ADD_CIRCLE,
                    #                 icon_color="blue",
                    #                 icon_size=50,
                    #                 tooltip="System processes",
                    #                 on_click=add_ps_button
                    #             ),
                    #         ],
                    #         alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    #     ),
                    # ),
                    ft.TextButton(
                        width=100,
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.FORMAT_LIST_BULLETED,
                                    icon_color="gray",
                                    icon_size=50,
                                    tooltip="List commands",
                                    on_click=list_button
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
