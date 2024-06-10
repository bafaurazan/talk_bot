""""""

import flet as ft

import requests


def SettingsView(page, ft=ft):


    url = 'http://127.0.0.1:8000/api/document/'

    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # print("Items:", data)
    else:
        print(f"Failed to retrieve items. Status code: {response.status_code}")




    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(data)
                ]
            )
        ]
    )

    return content
