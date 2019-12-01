# -*- coding: utf-8 -*-
from flask import render_template, request,redirect, url_for
from web_app.storage import BLOG_ENTRIES

def entry_page(key):
     error1=None
    for i in BLOG_ENTRIES:
        if key == i['key']:
            title = i['title']
            text_a  = i['text']
            comments = i['comments']

        if request.method == 'POST':
            name = request.form.get("name")
            text = request.form.get("text")
            if len(name)>0 and len(text)>0:
                i['comments'].append({"name": name, "text": text})
                return redirect(url_for('entry_page', key=key))
            else:
                 error1 = 'full fields'
    return render_template('entry.html', text=text_a, title=title, comments=comments,error1=error1)

