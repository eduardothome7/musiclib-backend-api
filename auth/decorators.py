import requests
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

def validate_token(r):
    @wraps(r)
    def decoration_function(*args, **kwargs):
        token = request.headers.get('Token')

        if not token:
            return jsonify({'message': 'Token não preenchido'}), 403

        url =  os.getenv('URL_AUTH_API') + '/auth/validate_token'
        headers = {"Token": token}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return r(*args, **kwargs)
            else:
                return jsonify({'message': 'Token inválido'}), 403
        except requests.exceptions.RequestException as e:
            return jsonify({'message': f'Erro ao validar token: {str(e)}'}), 500

    return decoration_function
