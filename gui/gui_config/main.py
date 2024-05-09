from time import sleep
import flet as ft
import pyautogui as pag
import ps_manager


def main(page: ft.Page):
   page.window_height = pag.size()[1]
   page.window_width = pag.size()[0] // 3


   page.window_top = 0
   page.window_left = pag.size()[0] - pag.size()[0]/3

   page.add(ft.SafeArea(ft.Text("testing")))

   page.title = "talk_bot"

   page.window_visible = True
   # page.window_resizable = False

   page.update()



ft.app(target=main, view=ft.FLET_APP_HIDDEN)
