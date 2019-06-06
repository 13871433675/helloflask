# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask, request, redirect, abort, make_response, json, url_for

app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, wangqizhi22!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Flask')
    return '<h1>Hello, Flask!</h1>' % name


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    #  重定向测试
    # return redirect('http://www.example.com')
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, commond say hello to qizhiHuman2!')


# 拦截器
@app.before_request
def before():
    print('test before')
    # return "test before"


@app.route('/404')
def not_found():
    abort(404)


@app.route('/test1')
def test():
    date = {
        "note": {
            "to": "Peter",
            "from": "Jane",
            "heading": "Remider",
            "body": "Don't forget the party!"
        }
    }
    jsondate = json.dumps(date)
    response = make_response(jsondate)
    response.mimetype = 'text/json'
    return response

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('test')))
    response.set_cookie('name', name)
    return response