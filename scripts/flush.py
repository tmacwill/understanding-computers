#!/usr/bin/env python

import memcache

cache = memcache.Client(['127.0.0.1:11211'])
cache.flush_all()
