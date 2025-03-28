from flask import Blueprint, request, jsonify
from models.song import Song, song_artist
from models.artist import Artist
from models import db
from auth.decorators import validate_token

songs_app = Blueprint('songs', __name__)

@songs_app.before_request
@validate_token
def before_request():
    pass

@songs_app.route('/songs', methods=['GET'])
def get_all():
    songs_artists = []
    artists = Artist.query.all()
    for artist in artists:
        artist_songs = {
            "artist_id" : artist.id,
            "name" : artist.name,
            "songs": [song.to_dict() for song in artist.songs]
        }

        songs_artists.append(artist_songs)

    return jsonify([song_artist for song_artist in songs_artists])

@songs_app.route('/songs/search', methods=['GET'])
def search():
    artist_id = request.args.get('artist_id', type=int)

    if not artist_id:
        return jsonify({"error": "artist_id is required"}), 400

    songs = Song.query.join(song_artist).filter(song_artist.c.artist_id == artist_id).all()

    return jsonify([song.to_dict() for song in songs])

@songs_app.route('/songs/<int:item_id>', methods=['GET'])
def get(item_id):
    item = Song.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@songs_app.route('/songs', methods=['POST'])
def add():
    data = request.get_json()
    new_item = Song(title=data['title'])

    if 'artist_id' in data:
        artists = [Artist.query.get(artist_id) for artist_id in data['artist_id']]
        new_item.artists = artists

    if 'file' in data:
        pass

    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@songs_app.route('/songs/<int:item_id>', methods=['PUT'])
def update(item_id):
    item = Song.query.get_or_404(item_id)
    data = request.get_json()
    item.title = data.get("title", item.title)

    # Se houver artistas no payload, atualize a lista de artistas
    if 'artists' in data:
        artists = [Artist.query.get(artist_id) for artist_id in data['artists']]
        item.artists = artists

    db.session.commit()
    return jsonify(item.to_dict())

@songs_app.route('/songs/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    item = Song.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Song deleted"})
