import flet as ft
from src.routes.router import navigate_to

def create_app(page: ft.Page):
    page.title = "BemStarE"
    
    # Define um tema padrão para a página
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,  # Cor principal para a sidebar e botões
            on_primary=ft.colors.WHITE,
            surface=ft.colors.LIGHT_BLUE,
            background=ft.colors.WHITE,
            on_background=ft.colors.BLACK,
        )
    )
    
    # Variável para armazenar o nome do usuário
    user_name = ""

    # Função para definir o nome do usuário após o login
    def set_user_name(name):
        nonlocal user_name
        user_name = name
        page.update()

    # Column dentro do Container onde o conteúdo dos ambientes será exibido
    content_column = ft.Column()
    content_container = ft.Container(content_column, width=600, padding=20, bgcolor=ft.colors.SURFACE)

    # Sidebar para navegação entre os ambientes
    sidebar = ft.Column(
        [
            ft.Image(src="/assets/default_avatar.png", width=50, height=50),  # Avatar padrão
            ft.Text("Olá, " + (user_name if user_name else "Visitante")),
            ft.ElevatedButton("Dicas e Informações", on_click=lambda e: navigate_to("info", content_column)),
            ft.ElevatedButton("Saúde Mental", on_click=lambda e: navigate_to("mental_health", content_column)),
            ft.ElevatedButton("Diversão", on_click=lambda e: navigate_to("fun_area", content_column)),
            ft.ElevatedButton("Sobre", on_click=lambda e: navigate_to("about", content_column)),
        ],
        alignment=ft.MainAxisAlignment.START,
    )
    
    # Layout da página principal
    page.add(
        ft.Row(
            [
                ft.Container(sidebar, width=200, padding=20, bgcolor=page.theme.color_scheme.primary),
                content_container,
            ],
            expand=True,
        )
    )

    # Inicia na tela de login e passa a função navigate_to
    navigate_to("login", content_column, set_user_name=set_user_name, navigate_to=navigate_to)
