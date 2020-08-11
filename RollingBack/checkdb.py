import sqlite3


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)


# for row in db.execute("select strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') as localtime,"
#                       " history.account, history.amount from history order by history.time"):

for row in db.execute("select * from localhistory"):
    print(row)

db.close()