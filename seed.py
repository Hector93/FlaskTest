#!/usr/bin/python3
import sys
import requests
import sqlite3

# sql statement for the creation of the users table
sqlUsersTable = 'CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY, username VARCHAR, ghid integer, image_url VARCHAR, ghtype VARCHAR, link VARCHAR);'
# sql statement for deleting previous data;INTO
sqlDeletePreviousEntries = 'DELETE FROM user;'

def createConnection():
    """ create a database connection to a database that resides
        in the same folder as this script
    :return: db connection
    """
    conn = None;
    try:
        conn = sqlite3.connect('app/users.db')
    except sqlite3.Error as e:
        print(e)
    finally:
        return conn

def createTable(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.execute(sqlDeletePreviousEntries)
    except sqlite3.Error as e:
        print(e)

def createUsers(conn, users):
    """ insert users in to the provided DB
    :param conn: Connection object
    :param users: list of users to be inserted in the database
    :return: lastrowid from the insert
    """
    sql = 'INSERT INTO user(username, ghid, image_url, ghtype, link) VALUES (?, ?, ?, ?, ?);'
    cursor = conn.cursor()
    cursor.executemany(sql, users)
    conn.commit()
    return cursor.lastrowid

def getUsers(nUsers=150, timeout=10):
    """ retrive the amount of users from github
    :param nUsers: total number of users to retrive default 150
    :param timeout: timeout for the requests default 10 seconds
    :return: list of users
    """
    #test if the requested users are more than 100 because
    #thats the max amount allowed per request
    maxAmount = 100

    if nUsers > maxAmount:
        parameters = {'per_page': maxAmount}
    else:
        parameters = {'per_page': nUsers}
    petitions = [maxAmount] * (int(nUsers/maxAmount) - 1)
    if nUsers%maxAmount != 0 and nUsers > maxAmount:
        petitions.append(nUsers%maxAmount)
    url = 'https://api.github.com/users'
    try:
        userRows = []
        response = requests.get(url, params=parameters, timeout=timeout)
        users = response.json()
        for petition in petitions:
            url = response.links['next']['url']
            response = requests.get(url, timeout=timeout)
            users = users + response.json()[:petition]
        for user in users:
            userRows.append((user['login'], user['id'], user['avatar_url'], user['type'], user['html_url']))
        return userRows
    except Exception as e:
        print('an error occured when retriving users: {}'.format(e))

def main(total=150):
    db = createConnection()
    createTable(db, sqlUsersTable)

    users = getUsers(total)
    createUsers(db, users)

if __name__ == '__main__':
    args = sys.argv
    total = 150
    if len(args) == 2:
        total = int(args[1])
    print(total)
    main(total)
