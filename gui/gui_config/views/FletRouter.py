"""Routing managment"""

import flet as ft

from views.index_view import IndexView
from views.settings_view import SettingsView
from views.add_ps_view import AddPSView
from views.add_command_view import AddCommandView


class Router:
    """Class managing different route views, allowing SPA for multiple sections"""

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page), # main page of the app
            "/settings": SettingsView(page), # settings
            "/add_ps": AddPSView(page), # add one of the currently open system processes
            "/add_command": AddCommandView(page) # add command
        }
        self.body = ft.Container(content=self.routes['/'])


    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
