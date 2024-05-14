""""""

import flet as ft

from views.ps_manager import ps_manager as ps_m


def AddPSView(page, ft=ft):

    data = ps_m

    # TODO IN PROGRESS
    content = ft.SearchBar(
        view_elevation=4,
        bar_hint_text="Znajdź PS...",
        # on_change=
    )

    return content
