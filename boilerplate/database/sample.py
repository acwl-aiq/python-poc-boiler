from boilerplate.database.connection import DBConnection


def add_test_entry(id_: str, val: str):
    with DBConnection() as conn:
        cur = conn.cursor()
        print(f"XXX {val} {len(val)}")
        cur.execute(f"INSERT INTO test (unique_id, some_value, update_time) VALUES ('{id_}', '{val}', now());")
        cur.close()
