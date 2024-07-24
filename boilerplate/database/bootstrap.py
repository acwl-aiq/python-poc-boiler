from boilerplate.database.connection import DBConnection


def create_tables():
    with DBConnection() as conn:
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS test (unique_id VARCHAR(36) PRIMARY KEY, some_value VARCHAR(36) NOT NULL, update_time TIMESTAMPTZ NOT NULL);"
        )
        cur.close()


def drop_tables():
    with DBConnection() as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS test;")
        cur.close()
