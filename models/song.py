from models import db

song_artist = db.Table(
    'song_artist',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artists = db.relationship('Artist', secondary=song_artist, backref=db.backref('songs', lazy='dynamic'))

    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title,
            "artists": [artist.to_dict() for artist in self.artists]
        }
