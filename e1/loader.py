import json
import hashlib
import os
import markdown
import re
import settings
import solr
import yaml
from bs4 import BeautifulSoup

from collections import OrderedDict

_chapters = None
_psets = None
_toc = None

def chapters():
    """
    Load chapter data from markdown source
    """

    global _chapters, _toc

    # if already loaded, use that
    if _chapters:
        return _chapters

    # if build exists for chapters, then use that
    if os.path.exists(settings.CHAPTER_BUILD):
        with open(settings.CHAPTER_BUILD, 'r') as f:
            _chapters = OrderedDict(sorted(json.load(f).items(), key=lambda e: int(e[1]['sequence'])))
            return _chapters

    # make sure table of contents exists
    toc()

    # load chapter metadata
    _chapters = OrderedDict()
    with open(settings.CHAPTER_METADATA) as f:
        info = yaml.load(f)
        for i, chapter in enumerate(info):
            # add entry for each chapter
            chapter_id = chapter['id']
            _chapters[chapter_id] = {
                'sequence': i
            }

            # add other chapter metadata
            for k, v in chapter.iteritems():
                _chapters[chapter_id][k] = v

    # iterate over markdown source for each chapter in metadata
    for i in _chapters.iterkeys():
        with open(settings.CHAPTER_SRC + '/' + i + '.markdown') as f:
            # compile markdown to html
            content = f.readlines()
            for line in content[:]:
                # extract subheadings
                if re.match(r'^## ', line):
                    _toc[i]['subheadings'].append({
                        'id': subheading(line),
                        'subheading': line[3:-1]
                    })

            _chapters[i]['content'] = markdown.markdown("".join(content))

    # write build files
    with open(settings.CHAPTER_BUILD, 'w') as f:
        json.dump(_chapters, f)
    with open(settings.TOC_BUILD, 'w') as f:
        json.dump(_toc, f)

    return _chapters

def solr_load():
    """
    Load content into solr
    """

    global _chapters

    # initialize solr connection
    conn = solr.Solr(settings.SOLR_URL)

    # wipe solr
    conn.delete_query('*:*')

    # ensure that chapters are loaded
    chapters()

    for i in _chapters.iterkeys():
        solr_load_chapter(conn, i, _chapters[i])

def solr_load_chapter(conn, title, chapter):
    """
    Load chapter into solr
    Args:
        conn - solr connection object
        title - title of chapter
        chapter - chapter object to load
    """

    # split chapter into subchapters
    soup = BeautifulSoup(chapter['content'])

    for header in soup.find_all('h2'):
        # get header and format subheading
        subtitle = title + '/' + header.text.replace(' ', '-').lower()
        text = ''

        nextSib = header.nextSibling

        while True:
            # if done, break
            if nextSib is None:
                break
            try:
                nextName = nextSib.name
                if nextName == 'h2':
                    break
                text = text + nextSib.text
                nextSib = nextSib.nextSibling
            # handle navigable strings
            except:
                text = text + str(nextSib)
                nextSib = nextSib.nextSibling

        doc = {
            'id': subtitle,
            'title': title,
            'text': text
        }

        conn.add(doc, commit=True)


def psets():
    """
    Load all psets
    """

    global _toc, _psets

    # table of contents already generated, so use that
    if _psets:
        return _psets

    # if build exists for psets, then use that
    if os.path.exists(settings.PSET_BUILD):
        with open(settings.PSET_BUILD, 'r') as f:
            _psets = json.load(f)
            return _psets

    # make sure table of contents exists
    toc()

    # load psets from yaml source
    _psets = {}
    _psets['questions'] = OrderedDict()
    _psets['answers'] = {}
    _psets['points'] = {}

    #for i in _toc.iterkeys():
    for i in ['graphics']:
        with open(settings.PSET_SRC + '/' + i + '.yaml') as f:
            _psets['questions'][i] = yaml.load(f)

        # store answers for each question
        total_points = 0
        for question in _psets['questions'][i]:
            # top-level question, so hash on text
            if 'question' in question:
                # determine question id
                question_id = hashlib.sha1(i + question['question']).hexdigest()
                question['id'] = question_id

                # store answer to question
                if 'answer' in question:
                    _psets['answers'][question_id] = {
                        'answer': question['answer'],
                        'points': question['points'],
                        'pset': i
                    }

                    # keep track of total points
                    total_points += question['points']

            # sequence, so hash on each question
            elif question['type'] == 'sequence':
                for q in question['questions']:
                    # determine question id
                    question_id = hashlib.sha1(i + q['question']).hexdigest()
                    q['id'] = question_id

                    # store answer to question
                    _psets['answers'][question_id] = {
                        'answer': q['answer'],
                        'points': q['points'],
                        'pset': i
                    }

                    # keep track of total points
                    total_points += q['points']

        # store total points for pset
        _psets['points'][i] = total_points

    # write build file
    with open(settings.PSET_BUILD, 'w') as f:
        json.dump(_psets, f)

    return _psets

def subheading(s):
    """
    Construct a subheading ID from subheading text
    """

    return s[3:-1].replace(' ', '-').lower()

def toc():
    """
    Load table of contents from metadata
    """

    global _toc

    # table of contents already generated, so use that
    if _toc:
        return _toc

    # if build exists for table of contents, then use that
    if os.path.exists(settings.TOC_BUILD):
        with open(settings.TOC_BUILD, 'r') as f:
            _toc = OrderedDict(sorted(json.load(f).items(), key=lambda e: int(e[1]['sequence'])))
            return _toc

    # build doesn't exist, so need to generate
    _toc = OrderedDict()
    with open(settings.CHAPTER_METADATA) as f:
        # load yaml contents
        info = yaml.load(f)
        for i, chapter in enumerate(info):
            # create entry in table of contents
            chapter_id = chapter['id']
            _toc[chapter_id] = {
                'heading': chapter['title'],
                'sequence': i,
                'subheadings': [],
                'tags': chapter['tags']
            }

    # write build file
    with open(settings.TOC_BUILD, 'w') as f:
        json.dump(_toc, f)

    return _toc
