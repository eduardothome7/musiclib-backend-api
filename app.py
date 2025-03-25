from flask import Flask
from controllers.artists_controller import app as artist_app
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musiclib_api.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
app.register_blueprint(artist_app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
