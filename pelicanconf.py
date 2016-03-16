#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Casey J Law'
SITENAME = u'Casey J Law'
SITEURL = 'http://caseyjlaw.github.io'
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
GOOGLE_ANALYTICS = u'UA-3920334-4'
#PROFILE_IMAGE_URL = 'https://drive.google.com/file/d/1JA_IufQKREG4Sw1qsrpTPDyi6wFJw-gR2g/view?usp=sharing'
#COVER_IMAGE_URL = 'https://drive.google.com/file/d/1JA_IufQKREG4Sw1qsrpTPDyi6wFJw-gR2g/view?usp=sharing'
THEME = 'elegant'
MARKUP = ('md', 'ipynb')

LANDING_PAGE_ABOUT = {
#    'title': 'Casey J Law',
    'details': 'An Astronomer in the UC Berkeley Radio Astronomy Lab. I am interested in fast radio transients, data-intensive science, Python, and Civic Hacking.' # <img width=200 align="right" src="images/casey_vla.jpg">
    }
PROJECTS = [
    {'name': 'Fast Imaging with Radio Interferometers',
     'url': 'http://labs.adsabs.harvard.edu/adsabs/abs/2015ApJ...807...16L',
     'description': 'Using radio interferometers as high-speed cameras to capture millisecond impulses from rare transients like fast radio bursts, pulsars, and stars.'
     },
    {'name': 'VLA "realfast" project',
     'url': 'https://caseyjlaw.github.io/realfast',
     'description': 'Developing the Very Large Array as a real-time, commensal transient search platform.'
     },
    {'name': 'VLA Sky Survey',
     'url': 'https://science.nrao.edu/science/surveys/vlass',
     'description': 'I am co-chair of the technical working group for an ambitious new sky survey with the world\'s most sensitive radio interferometer.'
     }
    ]

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('tags', 'categories','archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['ipynb', 'render_math', 'sitemap', 'tipue_search', 'extract_toc']
STATIC_PATHS = ['extra/favicon.ico', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

HOME_EXCLUDE = True
DEFAULT_PAGINATION = False
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
