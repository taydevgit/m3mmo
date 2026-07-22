import sqlite3

def init_db():
    # create a database
    conn = sqlite3.connect("m3mmory.db")

    # make a cursor object to inject SQL
    cur = conn.cursor()

    # create and define the tables if they do not exist
    cur.execute("CREATE TABLE IF NOT EXISTS reminders(id INTEGER PRIMARY KEY, title TEXT, date TEXT, time TEXT, location TEXT, complete INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS groceries(id INTEGER PRIMARY KEY, item TEXT, date_bought TEXT, expires TEXT, price TEXT, notified INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS recipes(id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, link TEXT, notes TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS misc(id INTEGER PRIMARY KEY, content TEXT, created TEXT)")

    # return the value of the connection and the cursor object whenever this is called
    return conn, cur


# close when we are done with the bot? maybe this needs to be called from bot.py or something
# conn.close()