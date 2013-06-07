import re
from flask import abort, jsonify, render_template, request, session

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

    # TODO temporary until logins work
    user = db.session.query(User).filter_by(id=1).one()
    session['user'] = user

    user = session['user']

    # check if answer is correct
    answer = answers[question_id]
    correct = re.match(answer['answer'], request.form['answer']) != None

    # if question is correct and unanswered, user gets points
    count = db.session.query(Answer).filter_by(user_id=user.id).filter_by(question=question_id).\
            filter_by(correct=True).count()
    if count == 0 and correct:
        user.add_points(answer['points'])

    # log answer (for analytics)
    new_answer = Answer(question_id, user.id, request.form['answer'], correct)
    db.session.add(new_answer)
    db.session.commit()

    return util.json_success({
        'correct': correct,
        'points': answer['points'] if correct and count == 0 else 0
    })
