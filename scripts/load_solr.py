#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import e1.loader
e1.loader.solr_load()
