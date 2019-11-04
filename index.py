# -*- coding: utf-8 -*-
from flask import render_template
from web_app.storage import BLOG_ENTRIES
def index_page():
    articles=BLOG_ENTRIES




    return render_template('index.html',articles=articles)


