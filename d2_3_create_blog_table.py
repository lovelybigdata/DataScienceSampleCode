# -*- coding: utf-8 -*-

import sqlite3


def create_blog_table():

    # Paste Create Table Script HERE
    command = """

    DROP TABLE IF EXISTS "blog";
    CREATE TABLE "blog" ("content" TEXT, "author" TEXT, "photo" TEXT, "lat" DOUBLE, "lng" DOUBLE, "title" TEXT);
    INSERT INTO "blog" VALUES('不錯喔','Tim','http://i0.sinaimg.cn/travel/world/2008-12-12/U3403P704T2D44381F101DT20081212103743.jpg',23.33,33.44,NULL);
    INSERT INTO "blog" VALUES('很多東西可以吃','tim','http://ext.pimg.tw/mimg47/1391871607-3002859607.jpg',22,121,'台南雙日遊');

    """

    conn = sqlite3.connect('Blog.sqlite')
    c = conn.cursor()
    c.executescript(command)
    conn.commit()
