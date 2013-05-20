import json
import os
import markdown
import re
import settings
import yaml

from collections import OrderedDict
from e1.util import memoized

_chapters = None
_toc = None

def chapters():
    """
    Load chapter data from markdown source
    """

    global _chapters, _toc

    # if already loaded, use that
    if _chapters:
        return _chapters

    # make sure table of contents exists
    if not _toc:
        _toc = toc()

    # if build exists for chapters, then use that
    if os.path.exists(settings.CHAPTER_BUILD):
        with open(settings.CHAPTER_BUILD, 'r') as f:
            _chapters = OrderedDict(sorted(json.load(f).items(), key=lambda e: int(e[1]['sequence'])))
            return _chapters

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

            _chapters[i]['content'] = markdown.markdown("\n".join(content))

    # write build file
    with open(settings.CHAPTER_BUILD, 'w') as f:
        json.dump(_chapters, f)
    # write build file
    with open(settings.TOC_BUILD, 'w') as f:
        json.dump(_toc, f)

    return _chapters

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

def toc_list():
    """
    Build an HTML representation of the table of contents
    """

    global _toc

    # make sure table of contents exists
    if not _toc:
        _toc = toc()

    # build list of subheadings
    toc_list = '<ul>'
    for chapter_id, chapter in _toc.iteritems():
        # create list item for chapter
        toc_list += '<li><a href="/chapter/' + chapter_id + '">' + chapter['heading'] + '</a><ul>'

        # create entry for each subheading
        for subheading in chapter['subheadings']:
            toc_list += '<li><a href="/chapter/' + chapter_id + '/' + subheading['id'] + '">' + \
                subheading['subheading'] + '</a></li>'

        toc_list += '</ul></li>'
    toc_list += '</ul>'

    return toc_list