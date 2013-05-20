from flask import Flask
app = Flask(__name__)

import e1.loader

# load table of contents and chapters
e1.loader.toc()
e1.loader.chapters()

import e1.controllers.chapters
