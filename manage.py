#! /usr/bin/env python

from app import app
import os, stat, random
import argparse


class EnvironmentInjectionMiddleware:
    """Inject environment variable to Flask app"""

    allowed_meta_variables = ['REMOTE_USER', 'REMOTE_HOST']

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        for key, value in os.environ.items():
            if key in self.allowed_meta_variables or key.startswith('HTTP'):
                environ[key] = value

        return self.app(environ, start_response)


parser = argparse.ArgumentParser()
parser.add_argument("--host", default="127.0.0.1")
parser.add_argument("--port", default=5000, type=int)
args = parser.parse_args()

params = {
    'host': args.host,
    'port': args.port,
    'debug': True
}

app.wsgi_app = EnvironmentInjectionMiddleware(app.wsgi_app)
app.run(**params)
