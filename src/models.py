from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Assignment(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(), nullable=False)
    ordinal = db.Column(db.String(), nullable=False)
    correctnesses = db.Column(db.String(), nullable=False)
