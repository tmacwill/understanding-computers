import os

# app's base directory
BASE = os.path.dirname(os.path.realpath(__file__))

# directory for content source
CONTENT_SRC = BASE + '/content/src'

# directory for content builds
CONTENT_BUILD = BASE + '/content/build'

# directory for chapter markdown source
CHAPTER_SRC = CONTENT_SRC + '/chapters'

# file for chapter metadata
CHAPTER_METADATA = CONTENT_SRC +'/chapters.yaml'

# file for chapter build
CHAPTER_BUILD = CONTENT_BUILD + '/chapters.json'

# file for table of content build
TOC_BUILD = CONTENT_BUILD + '/toc.json'
