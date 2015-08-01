# -*- coding: utf-8 -*-
from bottle import route, template, view
import sqlite3


def blog_all():
    conn = sqlite3.connect('Blog.sqlite')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('select * from blog')
    return c.fetchall()  # You get a list of dict like object


@route('/blog_sql/')
@view('blog_template')
def blog_sql():

    return {
        "post_list": blog_all()
    }
