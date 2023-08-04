import pymysql.cursors
import os


DB_CONFIG = dict(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "negro"),
    password=os.environ.get("DB_PWD", "cgtadmin"),
    database=os.environ.get("DB_NAME", "stori"),
    charset="utf8",
    sql_mode="",
    cursorclass=pymysql.cursors.DictCursor,
)


class DB:
    def __init__(self):
        self.conn = None

    @property
    def cnx(self):
        if self.conn is None:
            try:
                self.conn = pymysql.connect(**DB_CONFIG)
            except Exception as e:
                print(f"ERROR: Could not connect to MySQL instance: {e}")
                exit()
        return self.conn

    def query(self, sql, *args):
        many = False
        if args:
            many = isinstance(args[0], list)
        with self.cnx.cursor() as cur:
            if many:
                cur.executemany(sql, args[0])
            else:
                cur.execute(sql, *args)
            return cur

    def one(self, sql, *args):
        cur = self.query(sql, *args)
        row = cur.fetchone()
        cur.close()
        return row

    def all(self, sql, *args):
        cur = self.query(sql, *args)
        rows = cur.fetchall()
        cur.close()
        return rows

    def create(self, sql, *args):
        cur = self.query(sql, *args)
        self.cnx.commit()
        cur.close()
        return self.cnx.affected_rows()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
