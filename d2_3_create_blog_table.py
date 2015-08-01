import sqlite3


def create_blog_table():

    # Paste Create Table Script HERE
    command = """
    """

    conn = sqlite3.connect('Blog.sqlite')
    c = conn.cursor()
    c.execute(command)
    conn.commit()
