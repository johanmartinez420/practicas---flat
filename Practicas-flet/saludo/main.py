import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.bgcolor="#2691B6"
ft.app(main)
