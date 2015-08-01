# -*- coding: utf-8 -*-

import shelve

d = shelve.open("blog", writeback=True)
d['post_list'] = [
        {
            'title': '台南雙日遊',
            'lat': 22,
            'lng': 121,
            'content': '很多東西可以吃',
            'photo': 'http://ext.pimg.tw/mimg47/1391871607-3002859607.jpg',
            'id': 0,
        },
    ]
