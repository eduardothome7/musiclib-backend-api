from models import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "user_id": self.user_id}
