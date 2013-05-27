import e1.loader as loader
import e1.settings as settings

from e1 import app
from flask import abort, jsonify, render_template

@app.route('/pset/<chapter>')
@app.route('/pset/<chapter>/<int:question>')
def pset(chapter, question=0):
    # make sure chapter is valid
    psets = loader.psets()
    if not chapter in psets:
        abort(404)

    # remove answers from each question
    pset = psets[chapter]
    for i in pset[:]:
        if 'answer' in i:
            del i['answer']

    return render_template('pset.html', pset=pset, chapter=chapter)
