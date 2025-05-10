import sqlite3
from contextlib import contextmanager

@contextmanager
def get_cursor():
    conn = sqlite3.connect('test_db.sqlite', check_same_thread=False)
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()  # Save changes after using the cursor
    finally:
        conn.close()


def create_post_tbl(cursor):
    cursor.execute("DROP TABLE tbl_posts")
    cursor.execute("CREATE TABLE tbl_posts(post_id INTEGER PRIMARY KEY AUTOINCREMENT, name text UNIQUE NOT NULL);")


def create_comments_tbl(cursor):
    # cursor.execute("DROP TABLE tbl_comments")
    cursor.execute("CREATE TABLE tbl_comments(comment_id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER , comment text UNIQUE NOT NULL, parent_comment_id INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(post_id) REFERENCES tbl_posts(post_id));")

