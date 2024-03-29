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
    'details': 'I am an astronomer at Caltech interested in radio transients, data-intensive astrophysics, and open science.' # <img width=200 align="right" src="images/casey_vla.jpg">
    }
PROJECTS = [
    {'name': 'Fast Radio Bursts',
     'url': 'https://ui.adsabs.harvard.edu/abs/2022ApJ...927...55L/abstract',
     'description': 'I am interested in understanding this mysterious new class of extragalactic, millisecond radio transient.'
     },
    {'name': 'OVRO Software and Algorithms Lab',
     'url': 'https://salab.caltech.edu',
     'description': 'I am leading development of software and algorithms at OVRO, especially for OVRO-LWA and DSA.'
     },
    {'name': 'VLA "realfast" project',
     'url': 'http://realfast.io',
     'description': 'I am leading an effort for real-time, commensal transient surveys at the Very Large Array.'
     },
    {'name': 'Slow Transients in Sky Surveys and Archives',
     'url': 'http://news.berkeley.edu/2018/10/04/ghost-objects-in-the-sky/',
     'description': 'I have led an effort to use radio sky surveys and archives to discover a decades-long, luminous radio transient.'
     }
    ]

#MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
DIRECT_TEMPLATES = (('tags', 'categories','archives', 'index', '404'))  # 'search' page has spinning wheel
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [nb_markup, 'sitemap', 'extract_toc']  # 'tipue_search' not working?
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
