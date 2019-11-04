# -*- coding: utf-8 -*-
from flask import render_template, request,redirect, url_for
from web_app.storage import BLOG_ENTRIES

def entry_page(key):
    for i in BLOG_ENTRIES:
        if key == i['key']:
            title = i['title']
            text = i['text']
            comments = i['comments']

        if request.method == 'POST':
            name = request.form.get("name")
            text = request.form.get("text")
            if len(name)>0 and len(text)>0:

                i['comments'].append({"name": name, "text": text})
                return redirect(url_for('entry_page', key=key))
    return render_template('entry.html', text=text, title=title, comments=comments)

