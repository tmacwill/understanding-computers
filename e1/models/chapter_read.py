from e1 import db

class ChapterRead(db.Model):
    __tablename__ = 'chapter_reads'

    # columns
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    chapter = db.Column(db.String(255))
    section = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)

    # relationsips
    user = db.relationship('User', backref=db.backref('chapter_reads', lazy='dynamic'))

    def __init__(self, user_id, chapter, section):
        self.user_id = user_id
        self.chapter = chapter
        self.section = section
