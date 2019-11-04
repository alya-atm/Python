# -*- coding: utf-8 -*-
from flask import render_template, request,redirect, url_for
import random
from web_app.storage import BLOG_ENTRIES

def create_entry_page():
    error = None

    if request.method == 'POST':
        key = str(random.randint(1000, 10000))
        title = request.form.get('title')
        text = request.form.get('text')
        created_at = datetime.datetime.now().str("%d/%m/%Y")
        if len(title)>0  and len(text)>0:
            BLOG_ENTRIES.append({
                'key': key,
                'title': title,
                'text': text,
                'created_at': created_at,
                'comments': [
                ]
            })
            return redirect(url_for('entry_page', key=key))
            return render_template('entry.html', title=title, text=text)
        else:
            error = 'full fields'
    return render_template('create_entry.html', error=error)
