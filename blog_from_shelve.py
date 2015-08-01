# -*- coding: utf-8 -*-
from bottle import route, template, view
import shelve


@route('/blog2/')
@view('blog_template')
def blog2():

    blog = shelve.open("blog")

    if 'post_list' not in blog:
        blog['post_list'] = []

    return dict(blog)
