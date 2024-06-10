"""Page view route displaying page listing the available commands in the database"""

import flet as ft

import requests

from .index_view import get_commands


def ListCommandsView(page, ft=ft):
    """
        Displays a list of buttons with
    """

    # url = 'http://127.0.0.1:8000/api/document/'

    # response = requests.get(url)

    # if response.status_code == 200:
    #     data = response.json()

    # else:
    #     print(f"Failed to retrieve items. Status code: {response.status_code}")
    #


    # cell_text = []

    # for i in range(0, len(get_commands())):
    #     cell_text.append()

    # content = ft.Column(
    #     [
    #         # ft.Text(get_commands())
    #         ft.DataTable(
    #             columns=[
    #                 t.DataColumn(ft.Text("Komenda"))
    #             ]
    #         )
    #     ],
    #     rows=[
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("John")),
    #                     ft.DataCell(ft.Text("Smith")),
    #                     ft.DataCell(ft.Text("43")),
    #             ],
    #     )]
    # )

    # json_data = get_commands()

    # def on_button_click(e):
    #     selected_value = e.control.text
    #     # Perform any action with the selected value
    #     print(f"Button clicked: {selected_value}")


    # def display_json_data(json_data):
    #     # Clear any existing controls
    #     page.controls.clear()

    #     if json_data:
    #         for item in json_data:
    #             # Assuming json_data is a list of dictionaries
    #             # and you want to display the value of the 'name' key
    #             name = item.get("command", 'No command')
    #             button = ft.Button(text=name, on_click=on_button_click)
    #             content.controls.append(button)


    # content = ft.Column(
    #     [
    #         display_json_data(json_data)
    #     ]
    # )

    data = get_commands()

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    count = 1

    for i in range(0, 60):
        lv.controls.append(ft.Text(f"Line {count}"))

    count += 1

    content = ft.Column(
        [
            lv
        ]
    )
    return content
