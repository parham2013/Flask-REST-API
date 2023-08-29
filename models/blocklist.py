from db import db


class BlockListModel(db.Model):
    __tablename__ = "blocklists"

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(320))
