# Mysql-Connector class

This **library** is made specially for mysql-connector python library for making easier mysql queries. It was used for several projects therefore it works without any problems.

## Installation

In order to start using this library, you should follow these steps.
1. First of all, install mysql-connector library in your working space
``` pip install mysql-connector``` 
2. After installation, download **Library.py** file
3. Implement this file to your project
4. The example of using it , you can see in **Example.py** file

## Usage 
This class with additional functions is easy to use. Before using it, you should fill **tables** variable with tables that will be in your database.
```Example: 
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
    }
}
```
**users** is the name of the table, **user_id, username, deposit_balance, withdraw_balance, referrals, channels** are column in the table. Near the column, we define type of column, NOT NULL or NULL, PRIMARY KEY and other settings for column. 
```
sql_connect(host,user,password)
``` 
This function connects to the mysql.
```
sql_install(database="new_database")
``` 
This function installs a database. If it does not exist, it will create the database. Moreover, it will use **tables** variable to set up the tables.
```
Example: users_table = sql_actions(table='users')
```
We initialize class sql_action and give the table name that we are going to work on. In our example, we define "users" table. It is necessary to fill **table** argument.
```
Example:  users_table.sql_insert(username='Joe',referral='5',withdraw_balance='105',deposit_balance='500')
```
**sql_insert** method inserts a record to the table. It is necessary to define what we are going to insert. Arguments should be filled like this: **column name = the value**. In our example we insert into username, referral, withdraw_balance and deposit_balance columns following values "Joe", 5, 105, 500. 
```
Example: users_table.sql_query(username="Joe",user_id='4')
```
**sql_query** method output all content of a row selected by specific criteria. In arguments, we should provide conditions, what kind of row we should find. It should be filled like this  **column name = the value**. As a result, we will receive array.
```
Example: users_table.sql_update(cond_column="username", cond_item='Joe', deposit_balance="5535")
```
**sql_update** method updates a row. In arguments we should provide condition column, condition item and the column with value that should be changed in row. Condition column is a column that the script should see in order to find necessary row to change, and by giving condition item, the script sees what row should be changed": **cond_column= Column , cond_item = Value that the row has in condition column**. After that, you define what should be changed by typing in arguments like that **column name = the value**
```
Example: users_table.sql_delete(cond_column="user_id", cond_item="4")
```
**sql_delete** method that deletes a row from table. We should provide condition column and condition item as we mentioned in **sql_update** method. Only cond_item and cond_column should be presented in order to find the specific row to delete.**cond_column= Column , cond_item = Value that the row has in condition column**
```
Example: users_table.sql_queryAll()
```
**sql_queryAll** method that will output all content of table. In our example, it will output everything that is in user table. No need any arguments.
```
Example: users_table.sql_QueryAllDesc()
```
**sql_QueryAllDesc** method just like **sql_queryAll** but it will return content of table in descending order, whereas **sql_queryAll** will output content in ascending order. 

## Contacts
Email: pilokmr@gmail.com
