# -*- coding: utf-8 -*-
"""
    flaskext.cors
    ~~~~~~~~~~~~~

    Adds CORS support to your application.

    :license: MIT, see LICENSE for more details.
"""


from flask import make_response, request, current_app


def cors(config=None):
    def init_default_config(config):
        config['CORS_ALLOWED_ORIGINS'] = config['CORS_ALLOWED_ORIGINS'] if 'CORS_ALLOWED_ORIGINS' in config and config['CORS_ALLOWED_ORIGINS'] is not None else '*'
        config['CORS_ALLOWED_METHODS'] = config['CORS_ALLOWED_METHODS'] if 'CORS_ALLOWED_METHODS' in config and config['CORS_ALLOWED_METHODS'] is not None else ['GET','POST','HEAD','OPTIONS']
        config['CORS_ALLOWED_HEADERS'] = config['CORS_ALLOWED_HEADERS'] if 'CORS_ALLOWED_HEADERS' in config and config['CORS_ALLOWED_HEADERS'] is not None else ['Origin','Accept','X-Requested-With','Content-Type','Access-Control-Request-Method','Access-Control-Request-Headers']
        config['CORS_EXPOSED_HEADERS'] = config['CORS_EXPOSED_HEADERS'] if 'CORS_EXPOSED_HEADERS' in config and config['CORS_EXPOSED_HEADERS'] is not None else None
        config['CORS_SUPPORT_CREDENTIALS'] = config['CORS_SUPPORT_CREDENTIALS'] if 'CORS_SUPPORT_CREDENTIALS' in config and config['CORS_SUPPORT_CREDENTIALS'] is not None else True
        config['CORS_PREFLIGHT_MAXAGE'] = config['CORS_PREFLIGHT_MAXAGE'] if 'CORS_PREFLIGHT_MAXAGE' in config and config['CORS_PREFLIGHT_MAXAGE'] is not None else 1800
        config['CORS_REQUEST_DECORATE'] = config['CORS_REQUEST_DECORATE'] if 'CORS_REQUEST_DECORATE' in config and config['CORS_REQUEST_DECORATE'] is not None else True

    
    if config is None:
        config = {}

    init_default_config(config)
