import flet as ft

def display(content_column):
    content_column.controls.append(
        ft.Column(
            [
                ft.Text("Dicas e Informações", size=24, weight="bold", color=ft.colors.PRIMARY),
                ft.ListView(
                    controls=[
                        ft.Text("Dica 1: Organize seu tempo de estudo", color=ft.colors.ON_SURFACE),
                        ft.Text("Dica 2: Pratique atividades físicas", color=ft.colors.ON_SURFACE),
                    ],
                ),
            ]
        )
    )
