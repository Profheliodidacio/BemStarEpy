import flet as ft
from src.api.chatbot_api import get_chatbot_response

def display(content_column):
    messages = ft.ListView(expand=True)
    input_field = ft.TextField(label="Digite sua mensagem", width=500)

    def send_message(e):
        messages.controls.append(ft.Text("Você: " + input_field.value, color=ft.colors.PRIMARY))
        response = get_chatbot_response(input_field.value)
        messages.controls.append(ft.Text("Chatbot: " + response, color=ft.colors.SECONDARY))
        input_field.value = ""
        content_column.update()

    content_column.controls.append(
        ft.Column(
            [
                ft.Text("Chat de Apoio Psicológico", size=24, weight="bold", color=ft.colors.PRIMARY),
                messages,
                ft.Row([input_field, ft.ElevatedButton("Enviar", on_click=send_message)]),
            ]
        )
    )
