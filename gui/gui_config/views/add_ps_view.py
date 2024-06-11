"""Page view route displaying a search for browsing and searching currently active system processes and to add them to database"""

import flet as ft
import json

from views.ps_manager import ps_manager as ps_m


def AddPSView(page, ft=ft):
    """Displays the search bar box with unfolding results that are adjusting to match given searched text"""

    ps_list = ps_m()

    # Temporarily saving to json
    def save_to_json(item):
        with open("ps_path.json", "w") as file:
            json.dump({"path": item}, file)
            file.write("\n")

    def search(e):
        query = search_bar.value.lower()
        filtered_items = [item for item in ps_list if query in item]
        list_view.controls.clear()
        for item in filtered_items:
            list_view.controls.append(ft.ListTile(title=ft.Text(item), on_click=lambda e, item=item: save_to_json(item)))
        list_view.update()



    list_view = ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text(item), on_click=lambda e, item=item: save_to_json(item)) for item in ps_list
        ]
    )

    search_bar = ft.SearchBar(
        view_elevation=4,
        bar_hint_text="Znajdź Proces...",
        on_change=search,
        width=300,
        controls=[
            list_view
        ]
    )


    content = ft.Column([
        search_bar
    ])


    return content
