from flask import Blueprint, request, jsonify
from models.artist import Artist
from models import db
from auth.decorators import validate_token

app = Blueprint('artists', __name__)

@app.before_request
@validate_token
def before_request():
    pass

@app.route('/artists', methods=['GET'])
def get_all():
    items = Artist.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/artists/<int:item_id>', methods=['GET'])
def get(item_id):
    item = Artist.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@app.route('/artists', methods=['POST'])
def add():
    data = request.get_json()
    new_item = Artist(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict(), 201)

@app.route('/artists/<int:item_id>', methods=['PUT'])
def update(item_id):
    item = Artist.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data.get("name", item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/artists/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    item = Artist.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Artist deleted"})

if __name__ == '__main__':
    app.run(debug=True)
