# -*- coding: utf-8 -*-
from bottle import route, run, template, view, debug


def article_compare(article1, article2):
    return article1['lat'] - article2['lat']


@route('/blog/')
@route('/')
@view('blog_template')
def hello():

    post_list = [
        {
            'title': '台南雙日遊',
            'lat': 22,
            'lng': 121,
            'content': '很多東西可以吃',
            'photo': 'http://ext.pimg.tw/mimg47/1391871607-3002859607.jpg',
            'id': 0,
        },
        {
            'title': '北海岸牛排',
            'lat': 25,
            'lng': 121,
            'content': '夫妻吵架，各開一家',
            'photo': 'http://ext.pimg.tw/mimg47/1391871607-3002859607.jpg',
            'id': 1,
        },
        {
            'title': 'yo',
            'lat': 24,
            'lng': 121,
            'content': '夫妻吵架，各開一家',
            'photo': 'http://ext.pimg.tw/mimg47/1391871607-3002859607.jpg',
            'id': 1,
        },
    ]

    post_list.sort(cmp=article_compare)

    return {
            'post_list': post_list
           }


if __name__ == "__main__":
    debug(True)
    run(host='localhost', port=8080, reloader=True)
