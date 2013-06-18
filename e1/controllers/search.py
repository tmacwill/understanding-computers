from flask import render_template

import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app
from e1.models import search as searchModel

@app.route('/search/<query>')
def query(query):
    """
    Search
    """

    results = searchModel.query(query)

    preparedResults = []

    # prepare results for viewing
    for result in results:
        preparedResult = {}
        preparedResult['id'] = result['id']
        preparedResult['text'] = results.highlighting[result['id']]['text'][0]
        preparedResults.append(preparedResult)

    # pass processed results to view
    return render_template('results.html', results=preparedResults, title='Search Results', subtitle=query)
