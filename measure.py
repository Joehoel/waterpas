from sense_hat import SenseHat
import sys
import getopt
import sense_hat
import mysql.connector as mariadb
from mysql.connector import errorcode
import time
sense = SenseHat()
orientation  = 0
pitch = [0, 0]
roll = [0, 0]
p = 0
r = 0
x = [0, 0]
y = [0, 0]
def save():
    dbconfig = {
        'user': 'water',
        'password': 'password',
        'host': 'localhost',
        'database': 'waterpas',
        'raise_on_warnings': True,
    }
    # parse arguments
    verbose = True
    interval = 10  # second
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vt:")
    except getopt.GetoptError as err:
        print(str(err))
        print('measure.py -q -t <interval>')
        print('-q: be quiet')
        print('-t <interval>: measure each <interval> seconds (default: 10s)')
        sys.exit(2)
    try:
        # instantiate a database connection
        try:
            mariadb_connection = mariadb.connect(**dbconfig)
            if verbose:
                print("Database connected")
            #database didn't connect properly ERROR HANDELING
        except mariadb.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("Error: {}".format(err))
            sys.exit(2)
        # create the database cursor for executing SQL queries
        cursor = mariadb_connection.cursor(buffered=True)

        # store measurement in database
        try:
            cursor.execute('INSERT INTO measurements (pitch, roll) VALUES (%s, %s);', (p, r))
            print('stored values', p,r)
        except mariadb.Error as err:
            print("Error: {}".format(err))

        else:
            # commit measurements
            mariadb_connection.commit()

            if verbose:
                print("Temperature committed")
            # close db connection
            cursor.close()
            mariadb_connection.close()

    except KeyboardInterrupt:
        pass
    
def do_thing(event):
    if event.action == 'pressed':
        print('You pressed me')
        save()

while True:
    sense.stick.direction_any = do_thing
    orientation = sense.get_orientation_degrees()
    if pitch:
        pitch.insert(1, pitch.pop(0))
    if roll:
        roll.insert(1, roll.pop(0))
    pitch[0] = orientation["pitch"]
    roll[0] = orientation ["roll"]
    p = round((pitch[0] + pitch[1]) / 2)
    r = round((roll[0] + roll[1]) / 2)
    print("pitch: ", p, "roll: ", r)
    
    sense.clear()
    if ((p < 10 and p > 0) or (p < 360 and p > 350)) and (r < 10 and r > 0) or (r < 360 and r > 350):
        xv = 0
        yv = 0
        while xv < 8:
            sense.set_pixel(xv,0,(0, 0, 255))
            sense.set_pixel(xv,7,(0, 0, 255))
            xv += 1
        while yv < 8:
            sense.set_pixel(0,yv,(0, 0, 255))
            sense.set_pixel(7,yv,(0, 0, 255))
            yv += 1
            
    if (p < 10 and p > 0) or (p < 360 and p > 350):
        x[0] = 3
        x[1] = 4
    else:
        if p > 330:
            x[0] = round((p - 330) / 10)
            x[1] = x[0] + 1
        elif p < 30:
            x[0] = round((p + 30) / 10)
            x[1] = x[0] + 1
    
    if (r < 10 and r > 0) or (r < 360 and r > 350):
        y[0] = 3
        y[1] = 4
    else:
        if r > 330:
            y[0] = 6 - round((r - 330) / 10)
            y[1] = y[0] + 1
        elif r < 30:
            y[0] = 6 - round((r + 30) / 10)
            y[1] = y[0] + 1
            
    sense.set_pixel(x[0], y[0], (0, 0, 255))
    sense.set_pixel(x[0], y[1], (0, 0, 255))
    sense.set_pixel(x[1], y[0], (0, 0, 255))
    sense.set_pixel(x[1], y[1], (0, 0, 255))
    
    time.sleep(0.1)

