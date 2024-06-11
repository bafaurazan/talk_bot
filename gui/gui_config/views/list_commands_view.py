"""Page view route displaying page listing the available commands in the database"""

import flet as ft

import requests

from .index_view import get_commands


def ListCommandsView(page, ft=ft):
    """
        Displays a list of available commands in the database as clickable buttons that evaluate the commands
    """

    data = get_commands()

    buttons = []
    for index, item in enumerate(data.get('items', [])):
        command = item.get('command', None)
        command_id = item.get('id', None)

        def button_click(e, command_id=command_id):
            url = f'http://localhost:8000/api/document/{command_id}/eval/'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

            else:
                print(f"Failed to retrieve items. Status code: {response.status_code}")


        button = ft.ElevatedButton(
            text=command,
            on_click=button_click
        )
        buttons.append(button)

    list_view = ft.ListView(
        controls=buttons,
        expand=True,
        spacing=10,
    )

    content = list_view



    return content
