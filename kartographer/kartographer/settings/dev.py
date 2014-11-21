"""Production settings and globals."""

from __future__ import absolute_import

from .production import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
# DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
# TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'http://static.kartographer.com/dev/assets/'
########## END STATIC FILE CONFIGURATION

# ########## TOOLBAR CONFIGURATION
# # See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
# INSTALLED_APPS += (
#     'debug_toolbar',
# )

# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# DEBUG_TOOLBAR_PATCH_SETTINGS = False

# # http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
# INTERNAL_IPS = ('127.0.0.1',)
# ########## END TOOLBAR CONFIGURATION
