# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

# email = 'petrov@gmail.com'

# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'John Doe'})

# cursor.execute("SELECT * FROM users")
# res = cursor.fetchone()
# res = cursor.fetchall()
#
# print(res)

# for user in res:
#     print(user[1], user[2])

# for user in res:
#     print(user['name'], user['email'])

# cursor.execute("INSERT INTO users (name, email) VALUES ('User 4', 'user4@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('User 5', 'user5@gmail.com')")
# db.commit()
#
# print(db.total_changes)

db.close()



