from app import db


class LBoardRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    score = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def tojson(self):
        res = dict()
        res["name"] = self.name
        res["score"] = self.score
        return res

