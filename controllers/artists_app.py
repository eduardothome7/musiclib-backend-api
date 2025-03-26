from flask import Blueprint, request, jsonify
from models.artist import Artist
from models import db
from auth.decorators import validate_token

artists_app = Blueprint('artists', __name__)

@artists_app.before_request
@validate_token
def before_request():
    pass

@artists_app.route('/artists', methods=['GET'])
def get_all():
    items = Artist.query.all()
    return jsonify([item.to_dict() for item in items])

@artists_app.route('/artists/<int:item_id>', methods=['GET'])
def get(item_id):
    item = Artist.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@artists_app.route('/artists', methods=['POST'])
def add():
    data = request.get_json()
    new_item = Artist(name=data['name'])
    new_item.user_id = data['user_id']
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict(), 201)

@artists_app.route('/artists/<int:item_id>', methods=['PUT'])
def update(item_id):
    item = Artist.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data.get("name", item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@artists_app.route('/artists/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    item = Artist.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Artist deleted"})