import os

# app's base directory
BASE = os.path.dirname(os.path.realpath(__file__))

# directory for content source
CONTENT_SRC = BASE + '/../content/src'

# directory for content builds
CONTENT_BUILD = BASE + '/../content/build'

# directory for chapter markdown source
CHAPTER_SRC = CONTENT_SRC + '/chapters'

# directory for psets yaml source
PSET_SRC = CONTENT_SRC + '/psets'

# file for chapter metadata
CHAPTER_METADATA = CONTENT_SRC +'/chapters.yaml'

# file for chapter build
CHAPTER_BUILD = CONTENT_BUILD + '/chapters.json'

# file for table of contents build
TOC_BUILD = CONTENT_BUILD + '/toc.json'

# file for psets build
PSET_BUILD = CONTENT_BUILD + '/psets.json'

# url for solr
SOLR_URL = 'http://localhost:8983/solr'

