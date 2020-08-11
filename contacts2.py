import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newanotherupdate@update.com"
phone = input("please enter hte phone umber")
# update_sql = "update contacts set email = '{}' where phone = {}".format(new_email, phone)
update_sql = "update contacts set email = ? where phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))
print("are connections the same: {}".format(update_cursor.connection == db))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("select * from contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.close()