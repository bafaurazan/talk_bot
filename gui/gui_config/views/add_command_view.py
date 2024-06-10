"""Page view route displaying a text box for user to add their own shell command to database"""

import flet as ft
import json


def AddCommandView(page, ft=ft):
    """Displays textbox with a button that after clicking adds a custom shell command to database"""

    input_textbox = ft.TextField(hint_text="Wpisz komendę...", width=300)

    # Temporarily saving to json
    def on_add_button_click(e):
        text_value = input_textbox.value
        data = {"command": text_value}
        with open("add_command.json", "w") as json_file:
            json.dump(data, json_file)


    add_button = ft.ElevatedButton(text="Dodaj", on_click=on_add_button_click)

    content = ft.Column([
        input_textbox,
        add_button
    ])



    return content
