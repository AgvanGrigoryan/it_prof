import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    if base:
        print('Database connected.')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, lang TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        r = cur.execute('SELECT * FROM users WHERE user_id=?', (data['user_id'],)).fetchone()
        base.commit()
        if r is None:
            cur.execute("INSERT INTO users VALUES (?, ?)", tuple(data.values()))
            base.commit()
        elif data['lang'] != r[1]:
            cur.execute('UPDATE users SET lang=? WHERE user_id=?', (data['lang'], data['user_id']))
            base.commit()
