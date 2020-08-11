import sqlite3
import datetime
import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("create table if not exists accounts (name text primary key not null, balance integer not null)")
db.execute("create table if not exists history (time timestamp not null,"
           " account text not null, amount integer not null, primary key (time, account))")
db.execute("create view if not exists localhistory as"
           " select strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') as localtime,"
           " history.account, history.amount from history order by history.time")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("select name, balance from accounts where (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("insert into accounts values(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        try:
            db.execute("update accounts set balance = ? where (name = ?)", (new_balance, self.name))
            db.execute("insert into history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("update accounts set balance = ? where (name = ?)", (new_balance, self.name))
            # db.execute("insert into history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount/100))
        return self._balance/100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("update accounts set balance = ? where (name = ?)", (new_balance, self.name))
            # db.execute("insert into history values(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount/100))
            return amount/100
        else:
            print("The amount muse be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance/100))



if __name__ == '__main__':

    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")
    db.close()
