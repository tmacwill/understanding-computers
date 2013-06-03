from e1 import settings
import solr

__conn = solr.Solr(settings.SOLR_URL)

def query(q):
    qString = 'text:'+q
    response = __conn.select.__call__(qString, highlight=['text'])
    return response
