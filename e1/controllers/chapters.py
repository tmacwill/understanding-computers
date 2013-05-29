import e1.loader as loader
import e1.settings as settings
import e1.util as util

from e1 import app, db
from e1.models.chapter_read import ChapterRead
from flask import render_template

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

    # if section not given, then use chapter as subheading
    if not section:
        section = chapters[chapter]['title'].replace(' ', '-').lower()

    return render_template('chapter.html', chapter_id=chapter, chapter=chapters[chapter], toc_list=toc_list)

@app.route('/read/<chapter>/<section>')
def read(chapter, section):
    """
    Mark a section as read
    """

    # add read to database
    read = ChapterRead(1, chapter, section)
    db.session.add(read)
    db.session.commit()

    return util.json_success()
