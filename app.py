# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from web_app.storage import BLOG_ENTRIES
from views.index import index_page
from views.create_entry import create_entry_page
from views.entry import entry_page
app = Flask(__name__)

app.add_url_rule('/', view_func=index_page, methods=['GET', 'POST'])
app.add_url_rule('/entry/<key>', view_func=entry_page,methods=['GET','POST'])
app.add_url_rule('/create', view_func=create_entry_page,methods=['GET','POST'])

if __name__ == '__main__':
    app.run()
