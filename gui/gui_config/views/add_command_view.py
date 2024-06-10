"""Page view route displaying a text box for user to add their own shell command to database"""

import flet as ft
import json
import requests

from views.ps_manager import ps_manager as ps_m



def AddCommandView(page, ft=ft):
    """Displays textbox with a button that after clicking adds a custom shell command to database"""

    ps_list = ps_m()


    command_input = ft.TextField(hint_text="Aktywator...", width=300, border_radius=50)

    documentation_input = ft.TextField(hint_text="Dokumentacja...", width=300, border_radius=50)

    def save_to_json(item):
        search_bar.value = item
        search_bar.update()
        list_view.controls.clear()
        list_view.update()


    def on_add_button_click(e):
        url = "http://localhost:8000/api/document/"

        data = {
            "command" : command_input.value,
            "request_path" : search_bar.value,
            "documentation" : documentation_input.value
        }

        json_data = json.dumps(data)

        response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})


    def search(e):
        query = search_bar.value.lower()
        filtered_items = [item for item in ps_list if query in item.lower()]
        list_view.controls.clear()
        for item in filtered_items:
            list_view.controls.append(ft.ListTile(title=ft.Text(item), on_click=lambda e, item=item: save_to_json(item)))
        list_view.update()


    def save_search(item):
        save_to_json(item)
        search_bar.value = ""  # Clear the search bar value
        search_bar.update()
        list_view.controls.clear()
        list_view.update()



    list_view = ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text(item), on_click=lambda e, item=item: save_to_json(item)) for item in ps_list
        ]
    )

    search_bar = ft.SearchBar(
        view_elevation=4,
        bar_hint_text="Proces...",
        on_change=search,
        width=300,
        # view_shape = CIRCLE,
        controls=[
            list_view,
        ]
    )

    add_button = ft.ElevatedButton(text="Dodaj", on_click=on_add_button_click)



    content = ft.Column([
        command_input,
        search_bar,
        documentation_input,
        add_button
    ])



    return content
