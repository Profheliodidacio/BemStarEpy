# BemStarE Py

BemStarE é um aplicativo de bem-estar para estudantes, desenvolvido com Flet e Python. Ele oferece um ambiente interativo onde os alunos podem acessar dicas, informações sobre saúde mental com um chatbot de psicologia, além de um espaço para diversão.

## Recursos
Login com Avatar: Tela inicial de login para identificar o usuário com um avatar personalizado.
Ambientes Interativos:
Dicas e Informações: Espaço para a escola compartilhar orientações e conteúdos úteis.
Saúde Mental: Ambiente de apoio psicológico com integração a um chatbot.
Área de Diversão: Espaço de entretenimento e jogos.
Página Sobre: Informações gerais sobre o aplicativo e seus objetivos.
## Requisitos
- Python 3.7+
- Flet (para construção de interfaces)
- Flask (opcional, caso o backend seja necessário)
## Estrutura do Projeto
```bash

BemStarEpy/
├── assets/                    # Imagens e recursos visuais do app
│   ├── logo.png               # Logo do BemStarE
│   ├── default_avatar.png     # Avatar padrão do usuário
├── src/
│   ├── api/                   # API para integração com o chatbot
│   │   └── chatbot_api.py
│   ├── screens/               # Telas do aplicativo
│   │   ├── info_tips_screen.py
│   │   ├── mental_health_screen.py
│   │   ├── fun_area_screen.py
│   │   ├── login_screen.py    # Tela de login
│   │   └── about_screen.py    # Tela sobre o aplicativo
│   ├── routes/                # Controle de navegação entre telas
│   │   └── router.py
│   └── main_app.py            # Configuração principal do app
├── main.py                    # Arquivo de entrada principal
├── README.md                  # Documentação do projeto
└── requirements.txt           # Lista de dependências do Python


```
# Instalação
1. Clone este repositório para sua máquina local:
```
bash

git clone https://github.com/Profheliodidacio/BemStarEpy.git
cd BemStarE
```

2. Crie um ambiente virtual e ative-o:
```
bash

python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

3. Instale as dependências listadas no requirements.txt:
```
bash

pip install -r requirements.txt
```
## Como Executar o Projeto
1. Execute o arquivo principal main.py:
```
bash

python main.py
ou
flet run BemStarE
```


2. O aplicativo abrirá no navegador por padrão, ou você poderá acessar o endereço exibido no terminal.

## Uso
Tela de Login: Digite seu nome para acessar o app. Um avatar padrão será exibido ao lado do seu nome.
Navegação: Use a barra lateral para navegar entre as seções:
Dicas e Informações: Veja as orientações e conteúdos publicados pela escola.
Saúde Mental: Converse com um chatbot de psicologia para suporte emocional.
Área de Diversão: Aproveite para descontrair com atividades e jogos.
Sobre: Acesse a página "Sobre" para saber mais sobre o propósito do BemStarE.

## Contribuição
Contribuições são bem-vindas! Se você deseja colaborar, siga as etapas abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch para a sua feature: git checkout -b feature/nome-feature.
3. Commit suas alterações: git commit -m 'Adiciona nova feature'.
4. Envie para o repositório: git push origin feature/nome-feature.
5. Abra um pull request.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

