from flask import session, render_template

import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app, db
from e1.models.chapter_read import ChapterRead
from e1.models.user import User

@app.route('/contents')
def contents():
    """
    Display the table of contents
    """

    toc = loader.toc()
    return render_template('contents.html', toc=toc)

@app.route('/chapter/<chapter>')
@app.route('/chapter/<chapter>/<section>')
def chapter(chapter, section=None):
    """
    Get the text of a chapter
    """

    # load chapters and table of contents
    chapters = loader.chapters()
    toc_list = loader.toc_list()
    toc = loader.toc()

    # if section not given, then use chapter as subheading
    if not section:
        section = chapters[chapter]['title'].replace(' ', '-').lower()

    return render_template('chapter.html', chapter_id=chapter, chapter=chapters[chapter], toc_list=toc_list, toc=toc)

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
    count = db.session.query(ChapterRead).filter_by(user_id = user.id).filter_by(chapter = chapter).\
            filter_by(section = section).count()
    if count == 0:
        user.points += settings.POINTS['section']

    # add read to database (for analytics)
    read = ChapterRead(user.id, chapter, section)
    db.session.add(read)
    db.session.commit()

    return util.json_success({ 'points': settings.POINTS['section'] if count == 0 else 0 })
