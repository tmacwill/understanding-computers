import re
from flask import abort, jsonify, render_template, request

import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app, db
from e1.models.user import User
from e1.models.answer import Answer

@app.route('/pset/<chapter>')
@app.route('/pset/<chapter>/<int:question>')
def pset(chapter, question=0):
    """
    Display the problem set for a chapter
    """

    # make sure chapter is valid
    questions = loader.psets()['questions']
    if not chapter in questions:
        abort(404)

    # temporary metadata
    toc = loader.toc()
    metadata = toc[chapter]

    # remove answers from each question
    pset = questions[chapter]
    for i in pset[:]:
        if 'answer' in i:
            del i['answer']

    return render_template('pset.html', pset=pset, chapter=chapter, metadata=metadata)

@app.route('/answer/<question_id>', methods=['POST'])
def answer(question_id):
    """
    Check if the answer to a question is correct
    """

    # make sure question is valid
    answers = loader.psets()['answers']
    if not question_id in answers:
        abort(404)

    # check if answer is correct
    correct = re.match(answers[question_id], request.form['answer']) != None

    # log answer
    answer = Answer(question_id, 1, request.form['answer'], correct)
    db.session.add(answer)
    db.session.commit()

    return util.json_success({ 'correct': correct })
