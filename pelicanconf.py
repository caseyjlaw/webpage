#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Casey J Law'
SITENAME = u'Casey J Law'
SITEURL = ''
SITESUBTITLE = 'stuff...'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

PATH = 'content'
SLUGIFY_SOURCE = 'title'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#SOCIAL = (('twitter', 'http://twitter.com/caseyjlaw'),
#          ('github', 'http://gibub.com/caseyjlaw'),)
GITHUB_URL = 'http://github.com/caseyjlaw'
TWITTER_URL = 'http://twitter.com/caseyjlaw'
#GOOGLE_ANALYTICS_ID = '3920334'

THEME = 'pelican-themes/gum'
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['ipynb']
STATIC_PATHS = ['extra/favicon.ico', 'notebooks']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

DEFAULT_PAGINATION = False
CACHE_CONTENT = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = True
