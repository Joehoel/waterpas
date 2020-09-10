#!/usr/bin/python

# import connection module; name it mariadb
import mysql.connector as mariadb
import json

# initialize
data = []

# connect to the database
mariadb_connection = mariadb.connect(
    user='water',
    password='password',
    database='waterpas')

# create a cursor object for executing queries
cursor = mariadb_connection.cursor()

# prepare a select query (last 100 items)
stmt = "SELECT id, pitch, roll FROM measurements ORDER BY id DESC LIMIT 20"

# execute the query (parameter must be a tuple)
cursor.execute(stmt)

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]

# returned rows (tuples)
rows = cursor.fetchall()

# sort the array, ascending
rows.sort(key=lambda x:x[0])

# close cursor and database
cursor.close()
mariadb_connection.close()


# create a json output format
output_json = {}
count = 0
for row in rows:
    
    output_json[count] = {'pitch' : row[1], 'roll' : row[2]}
    count += 1


print("Content-type: application/json\n")
print(json.dumps(output_json))
# done
