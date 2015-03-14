#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christina Koch'
SITENAME = u'enthusiasms'
SITEURL = 'http://christinalk.github.io/blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('My Website', 'http://christinalk.github.io'),
          ('My Twitter', 'http://twitter.com/_christinaLK'),)

DEFAULT_PAGINATION = 10

THEME = "gum"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
