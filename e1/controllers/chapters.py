from flask import g, session, render_template

import e1.models.badges as badges
import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app, cache, db
from e1.models.answer import Answer
from e1.models.chapter_read import ChapterRead

@app.route('/contents')
def contents():
    """
    View for the book's table of contents
    """

    # get total points for all problem sets
    psets = loader.psets()
    total_points = psets['points']

    # get all sections the user has read
    reads = g.user.get_reads()

    # get the user's points
    points = g.user.get_points()

    toc = loader.toc()
    return render_template('contents.html', toc=toc, reads=reads, points=points, total_points=total_points)

@app.route('/chapter/<chapter>')
@app.route('/chapter/<chapter>/<section>')
def chapter(chapter, section=None):
    """
    View for reading a single chapter
    """

    # load chapters and table of contents
    chapters = loader.chapters()
    toc = loader.toc()
    info = chapters[chapter]
    title = 'Chapter ' + str(info['sequence'] + 1)
    subtitle = info['title']

    return render_template('chapter.html', chapter_id=chapter, chapter=info, subtitle=subtitle, title=title, toc=toc)

@app.route('/progress')
def progress():
    """
    View for checking progress on site
    """

    # load info for progress
    toc = loader.toc()
    milestones = {}
    percentages = {}
    reads = g.user.get_reads()
    points = g.user.get_points()
    badge_progress = {}

    # determine which badges have been earned
    for k, v in g.all_badges.iteritems():
        if v['type'] == 'chapter':
            badge = badges.ChapterBadge(k, reads, points)
            badge_progress[k] = {
                'milestones': badge.milestones(),
                'percentage': badge.percentage(),
                'earned': badge.earned()
            }

    return render_template('progress.html', badge_progress=badge_progress, toc=toc)

@app.route('/read/<chapter>/<section>')
def read(chapter, section):
    """
    Mark a section as read
    """

    # if user hasn't read this section, then update points
    count = db.session.query(ChapterRead).filter_by(user_id=g.user.id).filter_by(chapter=chapter).\
            filter_by(section=section).count()
    if count == 0:
        g.user.add_points(settings.POINTS['section'])

    # add read to database (for analytics)
    read = ChapterRead(g.user.id, chapter, section)
    db.session.add(read)
    db.session.commit()

    return util.json_success({ 'points': settings.POINTS['section'] if count == 0 else 0 })
