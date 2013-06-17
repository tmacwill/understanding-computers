import e1.loader as loader

from collections import OrderedDict, defaultdict
from e1 import cache, db
from e1.models.answer import Answer
from e1.models.chapter_read import ChapterRead

class User(db.Model):
    __tablename__ = 'users'

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
        cache.delete('psets:points:' + str(self.id))

    def badges(self, reads=None, points=None):
        """
        Get all the badges that have been earned by the user
        reads -- What sections have been read
        points -- Which points have been earned
        """

        # check cache for badges
        earned_badges = cache.get('chapters:badges:' + str(self.id))
        if earned_badges:
            return earned_badges

        # make sure we have both reads and points
        if not reads:
            reads = self.reads()
        if not points:
            points = self.total_points()

        # load psets and table of contents
        earned_badges = OrderedDict()
        toc = loader.toc()
        psets = loader.psets()

        # sections mapping
        chapter_badges = OrderedDict()
        chapter_badges['hardware'] = ['powerup', 'binary', 'cpu', 'memory']
        chapter_badges['internet'] = ['internet', 'domains', 'protocols', 'email', 'tcpip']
        chapter_badges['multimedia'] = ['graphics', 'av']
        chapter_badges['security'] = ['onlinesec', 'datasec', 'privacy']
        chapter_badges['development'] = ['design', 'html', 'programming']

        # determine which badges have been earned
        earned_badges['chapters'] = True
        earned_badges['psets'] = True
        for badge, chapters in chapter_badges.iteritems():
            earned_badges[badge] = True
            for i in chapters:
                # check if all sections in a chapter are read
                if not i in reads or len(reads[i]) != len(toc[i]['subheadings']):
                    earned_badges[badge] = False
                    earned_badges['chapters'] = False

                # check if pset is complete
                if not i in points or points[i] != psets['points'][i]:
                    earned_badges[badge] = False
                    earned_badges['psets'] = False

        # complete badge if everything is done
        earned_badges['complete'] = earned_badges['chapters'] and earned_badges['psets']

        """
        # all badges
        earned_badges['initial'] = True
        earned_badges['hardware'] = True
        earned_badges['internet'] = True
        earned_badges['multimedia'] = True
        earned_badges['security'] = True
        earned_badges['development'] = True
        earned_badges['chapters'] = True
        earned_badges['pset'] = True
        earned_badges['complete'] = True
        """

        return earned_badges

    def reads(self):
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

    def total_points(self):
        """
        Get the total number of points earned by the user
        """

        # check cache for points
        points = cache.get('psets:points:' + str(self.id))
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

        # cache points for three hours
        cache.set('psets:points:' + str(self.id), points, timeout=3*60)

        return points
