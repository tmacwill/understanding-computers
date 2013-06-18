from e1 import settings
import solr

_conn = solr.Solr(settings.SOLR_URL)

def query(q):
    qString = 'text:' + q

    response = _conn.select.__call__(qString, highlight=['text'], hl_fragsize=400)
    return response
