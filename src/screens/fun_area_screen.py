import flet as ft

def display(content_column):
    content_column.controls.append(
        ft.Column(
            [
                ft.Text("Área de Diversão", size=24, weight="bold", color=ft.colors.PRIMARY),
                ft.Text("Aqui estão sugestões e jogos simples para relaxar", color=ft.colors.ON_SURFACE),
            ]
        )
    )
