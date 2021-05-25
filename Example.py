import mysql.connector
from mysql.connector import Error

# DB to fill
host = 'localhost'
user = 'root'
password = ''

tables = \
{
    'users':
    {
        'user_id':['integer', 'PRIMARY KEY','AUTO_INCREMENT'],
        'username':['text', 'NOT NULL'],
        'deposit_balance':['integer', 'NOT NULL'],
        'withdraw_balance':['integer', 'NOT NULL'],
        'referrals':['integer', 'NOT NULL'],
        'channels':['text', 'NULL'],
    },
    'channels':
    {
        'channel_id':['integer', 'PRIMARY KEY'],
        'channel_name':['text', 'NOT NULL'],
        'owner_id':['integer', 'NOT NULL'],
        'owner_name':['text', 'NOT NULL'],
    }
}

# The main class and functions
def sql_connect(h,u,p):
    global mydb
    try:
        mydb = mysql.connector.connect(
            host=h,
            user=u,
            passwd=p,
        )
        global mycursor
        mycursor = mydb.cursor()
        print("You have successfully connected")
    except Error:
        print("Wrong HOST or LOGIN or PASSWORD.")
        raise (SystemExit)

def sql_update(self,cond_column,cond_item,**kwargs):
    changes = ''
    for key, value in kwargs.items():
        changes = key+' = \''+value+'\','
    sqls = mycursor.execute("UPDATE "+self.table+" SET "+changes[:-1]+" WHERE "+cond_column+" = "+cond_item)
    mycursor.execute(sqls)
    mydb.commit()
    print("Info has been successfully updated")
def sql_delete(self,cond_column,cond_item):
    sqls = mycursor.execute("DELETE FROM "+self.table+" WHERE "+cond_column+" = "+cond_item)
    mycursor.execute(sqls)
    mydb.commit()
    print('Info has been successfully removed')

def sql_install(database):
    mycursor.execute("CREATE DATABASE IF NOT EXISTS "+database)
    mycursor.execute("USE "+database)
    for tablen in tables:
        def transform(x):
            def others(x2,y):
                v = ''
                try:
                    v = ' '+tables[x2][y][2]
                except:
                    pass
                return v
            result = ''
            for tablec in tables[x]:
                z = tablec + ' ' + tables[x][tablec][0] + ' ' + tables[x][tablec][1] + others(x,tablec)+','
                result += z
            return result

        mycursor.execute("""CREATE TABLE IF NOT EXISTS """+tablen+""" ("""+transform(tablen)[:-1]+""");""")
    print("Database has been successfully installed")


class sql_actions(object):
    def __init__(self,table):
        self.table = table
        def getId(tabl):
            for x in tables:
                if x == tabl:
                    for y in tables[x]:
                        return y
        self.id = getId(self.table)
    def sql_insert(self, **kwargs):
        keys = ''
        values = ''
        def strs(kwr):
            i = 0
            text = ''
            while i != len(kwr):
                text += '%s,'
                i += 1
            return text[:-1]
        for key, value in kwargs.items():
            keys += key + ','
            values += value + ' '
        sqlins = "INSERT INTO " + self.table + " (" + keys[:-1] + ") VALUES ("+strs(values.split())+")"
        mycursor.execute(sqlins, values.split())
        mydb.commit()
        print("Info has been successfully inserted")
    def sql_query(self,**kwargs):
        combined = ''
        for key, value in kwargs.items():
            combined = key+' = \''+value+'\' AND '
        mycursor.execute("SELECT * FROM "+self.table+" WHERE "+combined[:-5])
        result = mycursor.fetchall()
        print('You have gotten info')
        return result
    def sql_update(self,cond_column,cond_item,**kwargs):
        changes = ''
        for key, value in kwargs.items():
            changes = key+' = \''+value+'\','
        sqls = mycursor.execute("UPDATE "+self.table+" SET "+changes[:-1]+" WHERE "+cond_column+" = "+cond_item)
        mycursor.execute(sqls)
        mydb.commit()
        print("Info has been successfully updated")
    def sql_delete(self,cond_column,cond_item):
        sqls = mycursor.execute("DELETE FROM "+self.table+" WHERE "+cond_column+" = "+cond_item)
        mycursor.execute(sqls)
        mydb.commit()
        print('Info has been successfully removed')
    def sql_queryAll(self):
        mycursor.execute("SELECT * FROM "+self.table)
        result = mycursor.fetchall()
        print('You have gotten all info')
        return result
    def sql_QueryAllDesc(self, desc_cond):
        mycursor.execute("SELECT * FROM "+self.table+" ORDER BY "+ desc_cond +" DESC")
        result = mycursor.fetchall()
        print('You have gotten all info')
        return result



# The main example how to work with the library.

sql_connect(host,user,password)
sql_install(database="new_database")
users_table = sql_actions(table='users')
users_table.sql_insert(username='Joe',referral='5',withdraw_balance='105',deposit_balance='500')
print(users_table.sql_query(username="Joe",user_id='4'))
users_table.sql_update(cond_column="username", deposit_balance="5535", username='Joe')
users_table.sql_delete(cond_item="4", cond_column="user_id")