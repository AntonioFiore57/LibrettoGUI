import flet as ft
from view import View
from controller import Controller
import controller
def main(page: ft.Page):
    v = View(page)
    c = Controller(v)

    v.setController(c)





ft.app(target=main)
