#!/usr/bin/env python

import MySQLdb as sql
import memcache

connection = sql.connect('localhost', '', '', 'e1')
with connection:
    db = connection.cursor()
    db.execute('set FOREIGN_KEY_CHECKS = 0')
    db.execute('truncate answers')
    db.execute('truncate chapter_reads')
    db.execute('truncate users')

    db.execute('insert into users (name, email, photo, points) values ("Tommy MacWilliam", "tommy@quora.com", "https://profile-a.xx.fbcdn.net/hprofile-ash4/276230_545482888_1365231227_q.jpg", 0)')

cache = memcache.Client(['127.0.0.1:11211'])
cache.flush_all()
