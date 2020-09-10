import mysql.connector as mysql

config = {
    'user': 'user',
    'password': 'user',
    'host': 'localhost',
    'database': 'waterpas'
}

connection = mysql.connect(**config)
cursor = connection.cursor()

def insert(p,r):
    if p > 180:
        p = 360 - p
    else:
        p = 0 - p
    
    if r > 180:
        r = 360 - r
    else:
        r = 0 - r

    print("Inserted: (%s, %s)" % (p, r))
    cursor.execute("INSERT INTO waarden (pitch, roll) VALUES (%s, %s);", (p, r))
    connection.commit()
    
def get_all():
    cursor.execute("SELECT * FROM waarden;")
    values = cursor.fetchall()
    data = []
    for value in values:
        data.append({
            'id': value[0],
            'pitch': value[1],
            'roll': value[2],
            'time': value[3],
        })
    connection.commit()
    return data
