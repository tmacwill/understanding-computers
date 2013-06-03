from e1 import db

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.BigInteger, primary_key=True)
    question = db.Column(db.String(40))
    answer = db.Column(db.String(255))
    correct = db.Column(db.Boolean)

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('answers', lazy='dynamic'))

    def __init__(self, question, user_id, answer, correct):
        self.question = question
        self.user_id = user_id
        self.answer = answer
        self.correct = correct
