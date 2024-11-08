import flet as ft

def display(content_column):
    content_column.controls.clear()
    content_column.controls.append(
        ft.Column(
            [
                ft.Text("Sobre o BemStarE", size=24, weight="bold"),
                ft.Text("BemStarE é um aplicativo voltado para o bem-estar dos alunos, com áreas de dicas, apoio psicológico e diversão."),
                ft.Text("Desenvolvido para oferecer um ambiente de suporte, educação e entretenimento."),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )
    )
    content_column.update()
