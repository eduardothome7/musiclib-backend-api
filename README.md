## Instalação

1. Clone o repositório:

    git clone https://github.com/seu-usuario/musiclib-backend-api.git

    cd musiclib-backend-api

    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows

    pip install -r requirements.txt

    API_URL_DEV=http://localhost:8080
    API_URL_PROD=https://api.prod.com

    python3 app.py
