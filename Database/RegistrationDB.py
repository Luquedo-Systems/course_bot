import sqlite3 as sql

def save_code(user_id,code,email):
    con = sql.connect("./Database/DB_FOR_TBOT.db")
    cur = con.cursor()
    cur.execute("""Insert into User_code values(?,?,?)""",[user_id,code,email])
    con.commit()
    con.close()
    return user_id
def get_code(user_id):
    con = sql.connect("./Database/DB_FOR_TBOT.db")
    cur = con.cursor()
    cur.execute("""Select long_code from User_code
                where user_id=?""",[user_id])
    c=cur.fetchall()
    con.close()
    if(len(c)>0):
        return c[0][0]
    else:
        return None
def get_email(user_id):
    con = sql.connect("./Database/DB_FOR_TBOT.db")
    cur = con.cursor()
    cur.execute("""Select email from User_code
                where user_id=?""",[user_id])
    c=cur.fetchall()
    con.close()
    if(len(c)>0):
        return c[0][0]
    else:
        return None