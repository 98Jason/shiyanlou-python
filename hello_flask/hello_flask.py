#!/usr/bin/env python3

import flask

# Create the application
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """
    显示可在 '/' 访问的 index 页面
    """
    return flask.render_template('index.html')

@APP.route('/hello/<name>/')
def hello(name):
    """
    Displays the page greats who ever comse to visit it.
    """
    return flask.render_template('hello.html', name=name)

if __name__ == '__main__':
    APP.debug = True
    APP.run()
