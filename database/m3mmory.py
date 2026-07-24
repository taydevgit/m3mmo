import sqlite3

def init_db():
    conn = sqlite3.connect("m3mmory.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        name TEXT,
        date TEXT,
        time TEXT,
        location TEXT,
        complete INTEGER)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS grocery_lists(
        id INTEGER PRIMARY KEY,
        name TEXT,
        store TEXT,
        created TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS grocery_items(
        id INTEGER PRIMARY KEY,
        list_id INTEGER,
        item TEXT,
        quantity TEXT,
        category TEXT,
        checked INTEGER)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS recipes(
        id INTEGER PRIMARY KEY,
        name TEXT,
        ingredients TEXT,
        link TEXT,
        notes TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS links(
        id INTEGER PRIMARY KEY,
        label TEXT,
        url TEXT,
        category TEXT,
        note TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS bills(
        id INTEGER PRIMARY KEY,
        name TEXT,
        amount REAL,
        due_date TEXT,
        paid INTEGER,
        recurring INTEGER)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS subscriptions(
        id INTEGER PRIMARY KEY,
        name TEXT,
        amount REAL,
        renewal_date TEXT,
        category TEXT,
        active INTEGER)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS wishlist(
        id INTEGER PRIMARY KEY,
        title TEXT,
        url TEXT,
        priority TEXT,
        added_by TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS maintenance(
        id INTEGER PRIMARY KEY,
        item TEXT,
        last_done TEXT,
        next_due TEXT,
        notes TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS workout_plans(
        id INTEGER PRIMARY KEY,
        name TEXT,
        exercises TEXT,
        schedule TEXT,
        notes TEXT)""")

    conn.commit()
    return conn, cur