from flask import render_template

import e1.loader as loader
import e1.settings as settings
import e1.util as util
from e1 import app
from e1.models import search as searchModel

@app.route('/search/<query>')
def query(query):
    """
    Search over chapter contents
    """

    # query using search mode
    results = searchModel.query(query)
    preparedResults = []

    # prepare results for viewing
    for result in results:
        preparedResults.append({
            'id': result['id'],
            'text': results.highlighting[result['id']]['text'][0]
        })

    # pass processed results to view
    return render_template('results.html', results=preparedResults, title='Search Results', subtitle=query)
