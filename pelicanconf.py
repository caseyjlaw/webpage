#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Casey J Law'
SITENAME = u'Casey J Law'
SITESUBTITLE = ''
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

SOCIAL = (
    ('github-square', 'http://github.com/caseyjlaw'),
    ('twitter-square', 'http://twitter.com/caseyjlaw')
    )
TWITTER_USERNAME = 'caseyjlaw'
SOCIAL_PROFILE_LABEL = ''
#GITHUB_URL = 'http://github.com/caseyjlaw'
#TWITTER_URL = 'http://twitter.com/caseyjlaw'
GOOGLE_ANALYTICS_ID = 'UA-3920334-4'
#PROFILE_IMAGE_URL = 'https://drive.google.com/file/d/1JA_IufQKREG4Sw1qsrpTPDyi6wFJw-gR2g/view?usp=sharing'
#COVER_IMAGE_URL = 'https://drive.google.com/file/d/1JA_IufQKREG4Sw1qsrpTPDyi6wFJw-gR2g/view?usp=sharing'
THEME = 'pelican-themes/elegant'
MARKUP = ('md', 'ipynb')

LANDING_PAGE_ABOUT = {
    'title': 'Casey J Law',
    'details': 'An Astronomer in the UC Berkeley Radio Astronomy Lab. I am interested in fast radio transients, data-intensive science, Python, and Civic Hacking.'
    }
PROJECTS = [
    {'name': 'Fast Imaging with Radio Interferometers',
     'url': '',
     'description': 'Using radio interferometers as high-speed cameras to capture millisecond impulses from rare transients like fast radio bursts, pulsars, and stars.'
     },
    {'name': 'Real-time data analysis',
     'url': '',
     'description': 'Developing the Very Large Array as a real-time, commensal transient search platform.'
     }
    ]
        

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['ipynb', 'render_math', 'sitemap', 'tipue_search', 'extract_toc']
STATIC_PATHS = ['extra/favicon.ico', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

HOME_EXCLUDE = True
DEFAULT_PAGINATION = False
CACHE_CONTENT = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
