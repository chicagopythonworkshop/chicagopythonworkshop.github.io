#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sheila Miguez'
SITENAME = u'Chicago Pythonistas'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
          ('ChicagoPythonistas Meetup', 'http://www.meetup.com/ChicagoPythonistas/'),
          ('OpenHatch', 'http://openhatch.org/blog/'),
          ('The In-Person Event Handbook', 'http://opensource-events.com/'),
          ('Open Source Comes to Campus', 'http://campus.openhatch.org/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False
CC_LICENSE = 'CC-BY'
DEFAULT_PAGINATION = 10

#THEME = 'pelican-bootstrap3'
#TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
