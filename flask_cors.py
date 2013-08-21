# -*- coding: utf-8 -*-
"""
    flaskext.cors
    ~~~~~~~~~~~~~

    CORS middleware, adds CORS support to your application.

    :author: Mohit Soni
    :license: MIT, see LICENSE for more details.
"""


class CORSMiddleware(object):
    """Wrap the application in this middleware.

    :param app: the WSGI application
    :param app_root: Defaulting to ``'/'``, you can set this to something else
        if your app is mounted somewhere else.
    :param cors_config: the configuration
    """
    def __init__(self, app, app_root='/', cors_config=None):
        self.app = app
        self.app_root = app_root
        self.cors_config = cors_config

    def __call__(self, environ, start_response):
        # Check for the presence of 'Origin' header
        if 'HTTP_ORIGIN' in environ.keys():
            # Wrap it, to add CORS specific headers
            def _cors_start_response(status, headers, *args):
                """
                Add CORS headers here
                """
                headers = []

                return start_response(status, headers, *args)
            return self.app(environ, _cors_start_response)
        else:
            # Otherwise, let it be a pass through
            return self.app(environ, start_response)