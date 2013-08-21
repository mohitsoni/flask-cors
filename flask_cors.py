# -*- coding: utf-8 -*-
"""
    flaskext.cors
    ~~~~~~~~~~~~~

    CORS middleware, adds CORS support to your application.

    :author: Mohit Soni
    :license: MIT, see LICENSE for more details.
"""

import urlparse


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
        request_type = self.check_request_type(environ)
        if request_type in (CORSMiddleware.REQUEST_TYPE_SIMPLE, CORSMiddleware.REQUEST_TYPE_ACTUAL, CORSMiddleware.REQUEST_TYPE_PRE_FLIGHT):
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

    def check_request_type(self, environ):
        request_type = CORSMiddleware.REQUEST_TYPE_INVALID_CORS

        if environ is None:
            raise TypeError

        origin_header = environ['HTTP_ORIGIN'] if 'HTTP_ORIGIN' in environ.keys() else None

        if origin_header and self.is_valid_origin(origin_header):
            method = environ['REQUEST_METHOD']
            if method and method in CORSMiddleware.HTTP_METHODS:
                if 'OPTIONS' == method:
                    pass
                elif method in ('GET', 'HEAD'):
                    request_type = CORSMiddleware.REQUEST_TYPE_SIMPLE
                elif 'POST' == method:
                    content_type = environ['CONTENT_TYPE']
                    if content_type is not None:
                        content_type = content_type.lower().strip()
                        if content_type in CORSMiddleware.SIMPLE_HTTP_REQUEST_CONTENT_TYPE_VALUES:
                            request_type = CORSMiddleware.REQUEST_TYPE_SIMPLE
                        else:
                            request_type = CORSMiddleware.REQUEST_TYPE_ACTUAL
                elif method in CORSMiddleware.COMPLEX_HTTP_METHODS:
                    request_type = CORSMiddleware.REQUEST_TYPE_ACTUAL
        else:
            request_type = CORSMiddleware.REQUEST_TYPE_NOT_CORS

        return request_type

    def is_valid_origin(self, origin):
        is_valid = True

        if not origin:
            is_valid = False
        elif origin.find('%') != -1:
            # Checks for encoded characters. Helps prevent CRLF injection.
            is_valid = False
        elif '\r' in origin:
            # Detect CRLF characters
            is_valid = False
        elif '\n' in origin:
            # Detect CRLF characters
            is_valid = False
        else:
            try:
                parts = urlparse.urlsplit(origin)

                if parts is None or parts.scheme is None:
                    is_valid = False
            except:
                is_valid = False

        return is_valid

    
    # Request types
    REQUEST_TYPE_SIMPLE = 1
    REQUEST_TYPE_ACTUAL = 2
    REQUEST_TYPE_PRE_FLIGHT = 3
    REQUEST_TYPE_NOT_CORS = 4
    REQUEST_TYPE_INVALID_CORS = 5

    """
    Tuple of HTTP methods. Case sensitive.
    
    http://tools.ietf.org/html/rfc2616#section-5.1.1
    """
    HTTP_METHODS = ("OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT")

    """
    Tuple of Simple HTTP request headers. Case in-sensitive.

    http://www.w3.org/TR/cors/#terminology
    """
    SIMPLE_HTTP_REQUEST_CONTENT_TYPE_VALUES = ("application/x-www-form-urlencoded", "multipart/form-data", "text/plain")

    """
    Tuple of non-simple HTTP methods. Case sensitive.
    """
    COMPLEX_HTTP_METHODS = ("PUT", "DELETE", "TRACE", "CONNECT")