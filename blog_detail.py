# -*- coding: utf-8 -*-
from bottle import route, template, view
import sqlite3


def get_by_id(id):
    command = """ SELECT * FROM  blog  WHERE rowid={} """
    ## Add Code here to get the first article
    return c.fetchone()

#  http://localhost:8080/detail/1/

@route('/detail/<id:int>/')
@view('blog_detail')
def detail(id):

    return {
        'post': get_by_id(id)
    }
