import e1.loader as loader
from flask import g, session
from e1 import app, db
from e1.models.user import User

@app.before_request
def before_request():
    # TODO temporary until logins work
    user = db.session.query(User).filter_by(id=1).one()
    session['user'] = user

    # get info for all badges
    g.all_badges = loader.badges()

    # get currently logged-in user
    g.user = None
    if 'user' in session:
        g.user = session['user']
        g.user.badges = g.user.get_badges()
