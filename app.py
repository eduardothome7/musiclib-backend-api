from flask import Flask
from flask_cors import CORS
from controllers.artists_app import artists_app
from models import db
from flask_migrate import Migrate

app = Flask(__name__)

# Aplicando CORS globalmente, permitindo todos os métodos e cabeçalhos necessários
CORS(app, resources={r"/*": {
    "origins": "*",  # Permitir todas as origens
    "allow_headers": ["Content-Type", "Authorization", "Token"],  # Cabeçalhos permitidos
    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos permitidos
    "supports_credentials": True  # Permitir cookies/credenciais
}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musiclib_api.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(artists_app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
