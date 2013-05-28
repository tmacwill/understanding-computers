from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/e1'
db = SQLAlchemy(app)

import e1.loader

# load table of contents and chapters
e1.loader.toc()
e1.loader.chapters()
e1.loader.psets()

# load routes
import e1.controllers.chapters
import e1.controllers.questions
