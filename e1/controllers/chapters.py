from flask import session, render_template
from collections import defaultdict

import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app, cache, db
from e1.models.answer import Answer
from e1.models.chapter_read import ChapterRead
from e1.models.user import User

@app.route('/contents')
def contents():
    """
    Display the table of contents
    """

    # TODO temporary until logins work
    user = db.session.query(User).filter_by(id=1).one()
    session['user'] = user

    # get currently logged-in user
    user = session['user']

    # get reads for user, one per chapter/section pair
    all_reads = db.session.query(ChapterRead).filter_by(user_id=user.id).\
        group_by(ChapterRead.chapter, ChapterRead.section)

    # convert reads to hash for faster access
    reads = defaultdict(dict)
    for read in all_reads:
        reads[read.chapter][read.section] = True

    # get total points for all problem sets
    psets = loader.psets()
    total_points = psets['points']
    pset_answers = psets['answers']

    # check cache for points
    points = cache.get('psets:points:' + str(user.id))
    if not points:
        # get all of our correct answers
        answers = db.session.query(Answer).filter_by(user_id=user.id).\
            filter_by(correct=True).group_by(Answer.question)

        # tally scores for all psets
        points = defaultdict(int)
        for answer in answers:
            p = pset_answers[answer.question]['pset']
            points[p] += pset_answers[answer.question]['points']

        # cache points for three hours
        cache.set('psets:points:' + str(user.id), points, timeout=3*60)

    toc = loader.toc()
    return render_template('contents.html', user=user, toc=toc, reads=reads, points=points, total_points=total_points)

@app.route('/chapter/<chapter>')
@app.route('/chapter/<chapter>/<section>')
def chapter(chapter, section=None):
    """
    Get the text of a chapter
    """

    # load chapters and table of contents
    chapters = loader.chapters()
    toc = loader.toc()

    return render_template('chapter.html', chapter_id=chapter, chapter=chapters[chapter], toc=toc)

@app.route('/read/<chapter>/<section>')
def read(chapter, section):
    """
    Mark a section as read
    """

    # TODO temporary until logins work
    user = db.session.query(User).filter_by(id=1).one()
    session['user'] = user

    # get currently logged-in user
    user = session['user']

    # if user hasn't read this section, then update points
    count = db.session.query(ChapterRead).filter_by(user_id=user.id).filter_by(chapter=chapter).\
            filter_by(section=section).count()
    if count == 0:
        user.points += settings.POINTS['section']

    # add read to database (for analytics)
    read = ChapterRead(user.id, chapter, section)
    db.session.add(read)
    db.session.commit()

    return util.json_success({ 'points': settings.POINTS['section'] if count == 0 else 0 })
