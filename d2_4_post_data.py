import sqlite3


def post_data(title, photo, location, lat, lng, content):
    # add codes here
    command_template = """

    """
    insert_command = command_template.format(
        title, photo, location, lat, lng, content
        )

    print insert_command
    conn = sqlite3.connect("Blog.sqlite")
    conn.execute(insert_command)
    conn.commit()
