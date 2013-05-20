import e1.loader as loader
import e1.settings as settings

from e1 import app
from flask import render_template

@app.route('/contents')
def contents():
    toc = loader.toc()
    return render_template('contents.html', toc=toc)

@app.route('/chapter/<chapter>')
@app.route('/chapter/<chapter>/<section>')
def chapter(chapter, section=None):
    chapters = loader.chapters()
    toc_list = loader.toc_list()
    return render_template('chapter.html', chapter_id=chapter, chapter=chapters[chapter], toc_list=toc_list)
