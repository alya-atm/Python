import sqlite3
def commit_after_execute(con):
    def f2(f1):
        def wrapper(*args,**kwargs):
            return f1(*args,**kwargs)
        # Сохраняем изменения
        con.commit()
        return wrapper
    return f2

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS  users (id , username text)")
con.commit()

#Использование декоратора
@commit_after_execute(con)
def insert_in_table(object):
    cur = con.cursor()
    cur.execute('INSERT INTO users(id, username) VALUES(?, ?)', object)

insert_in_table((1,"Mike"))
cur.execute('SELECT * FROM users')
print(cur.fetchall())
