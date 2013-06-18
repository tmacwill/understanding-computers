from flask import jsonify
from bs4 import BeautifulSoup

def json_success(data={}):
    data['success'] = True
    return jsonify(data)

def stripHTML(text):
    if text is None:
        return None
    else:
        return ''.join(BeautifulSoup(text).findAll(text=True))

