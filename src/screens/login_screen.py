import flet as ft

def display(content_column, set_user_name, navigate_to):
    content_column.controls.clear()

    # Função para definir o nome do usuário e navegar para o conteúdo principal
    def on_login(e):
        set_user_name(name_field.value)
        navigate_to("info", content_column)

    # Campo de entrada do nome do usuário
    name_field = ft.TextField(label="Digite seu nome", width=400)
    login_button = ft.ElevatedButton("Entrar", on_click=on_login)

    # Estrutura do layout da tela de login
    content_column.controls.append(
        ft.Column(
            [
                ft.Image(src="/assets/logo.png", width=150),  # Exibe a logo
                ft.Text("Bem-vindo ao BemStarE", size=24, weight="bold"),
                name_field,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    content_column.update()
