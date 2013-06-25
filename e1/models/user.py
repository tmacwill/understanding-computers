import e1.loader as loader
import e1.settings as settings

from collections import OrderedDict, defaultdict
from e1 import cache, db
from e1.models.answer import Answer
from e1.models.badges import *
from e1.models.chapter_read import ChapterRead

class User(db.Model):
    # table name
    __tablename__ = 'users'

    # table columns
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    points = db.Column(db.Integer)

    def __init__(self, name, email, photo):
        self.name = name
        self.email = email
        self.photo = photo

    def add_points(self, points):
        """
        Add points to the user's score
        """

        self.points += points
        cache.delete('points:' + str(self.id))

    def get_badges(self, reads=None, points=None):
        """
        Get all the badges that have been earned by the user
        reads -- What sections have been read
        points -- Which points have been earned
        """

        # check cache for badges
        badges = cache.get('badges:' + str(self.id))
        if badges:
            return badges

        # make sure we have both reads and points
        if not reads:
            reads = self.get_reads()
        if not points:
            points = self.get_points()

        # load psets and table of contents
        all_badges = loader.badges()
        badges = OrderedDict()

        # determine which badges have been earned
        for k, v in all_badges.iteritems():
            if v['type'] == 'chapter':
                badges[k] = ChapterBadge(k, reads, points).earned()

        # cache badges
        cache.set('badges:' + str(self.id), badges, timeout=3*60)
        return badges

    def get_reads(self):
        """
        Get a hash of all sections the user has read
        """

        # get reads for user, one per chapter/section pair
        all_reads = db.session.query(ChapterRead).filter_by(user_id=self.id).\
            group_by(ChapterRead.chapter, ChapterRead.section)

        # convert reads to hash for faster access
        result = defaultdict(dict)
        for read in all_reads:
            result[read.chapter][read.section] = True

        return result

    def get_points(self):
        """
        Get the total number of points earned by the user
        """

        # check cache for points
        points = cache.get('points:' + str(self.id))
        if points:
            return points

        # get all answers to psets
        pset_answers = loader.psets()['answers']

        # get all of our correct answers
        answers = db.session.query(Answer).filter_by(user_id=self.id).\
            filter_by(correct=True).group_by(Answer.question)

        # tally scores for all psets
        points = defaultdict(int)
        for answer in answers:
            p = pset_answers[answer.question]['pset']
            points[p] += pset_answers[answer.question]['points']

        # cache points
        cache.set('points:' + str(self.id), points, timeout=3*60)
        return points
