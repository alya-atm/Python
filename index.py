# -*- coding: utf-8 -*-
from flask import render_template
from web_app.storage import BLOG_ENTRIES
def index_page():
    articles=BLOG_ENTRIES
    operation = request.args.get('operation')
    if operation == 'name':
        articles.sort(key=lambda x: x['title'])
    elif operation == 'date_new':
        articles.sort(key=lambda x: x['created_at'], reverse=True)
    elif operation == 'date_old':
        articles.sort(key=lambda x: x['created_at'])
    return render_template('index.html',articles=articles)

