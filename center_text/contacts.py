import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("create table if not exists contacts (name text, phone integer, email text)")
db.execute("insert into contacts(name, phone, email) values('Tim', 655678, 'tim@email.com')")
db.execute("insert into contacts values('Brian',1234,'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 20)



cursor.close()
db.commit()
db.close()

