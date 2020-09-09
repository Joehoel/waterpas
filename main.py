from sense_hat import SenseHat
import time
from db import insert

sense = SenseHat()

WHITE = (0, 0, 255)

pitch = [0,0]
roll = [0,0]
p = 0
r = 0
x = [0,1]
y = [0,1]


sense.stick.direction_any = lambda : insert(p,r)

# Draw the bubble on LED matrix
def draw():
    sense.set_pixel(x[0], y[0], WHITE)
    sense.set_pixel(x[0], y[1], WHITE)
    sense.set_pixel(x[1], y[0], WHITE)
    sense.set_pixel(x[1], y[1], WHITE)

# Loop
while True:

    # Get "pitch" and "roll" Values
    orientation = sense.get_orientation_degrees()
    if pitch:
        pitch.insert(1, pitch.pop(0))
    if roll:
        roll.insert(1, roll.pop(0))
    pitch[0] = orientation["pitch"]
    roll[0] = orientation ["roll"]
    # Get avarage
    p = round((pitch[0] + pitch[1]) / 2)
    r = round((roll[0] + roll[1]) / 2)

    # Clear matrix every iteration
    sense.clear()

    if p > 350 and p < 360:
        x[0] = 3
        x[1] = 4
    elif p > 340 and p < 350:
        x[0] = 2
        x[1] = 3
    elif p > 330 and p < 340:
        x[0] = 1
        x[1] = 2
    elif p < 10 and p > 0:
        x[0] = 3
        x[1] = 4
    elif p < 20 and p > 10:
        x[0] = 4
        x[1] = 5
    elif p < 30 and p > 20:
        x[0] = 5
        x[1] = 6
    elif p < 40 and p > 30:
        x[0] = 6
        x[1] = 7
    elif r > 350 and r < 360:
        y[0] = 3
        y[1] = 4
    elif r > 340 and r < 350:
        y[0] = 4
        y[1] = 5
    elif r > 330 and r < 340:
        y[0] = 5
        y[1] = 6
    elif r > 320 and r < 330:
        y[0] = 6
        y[1] = 7
    elif r < 10 and r > 0:
        y[0] = 4
        y[1] = 3
    elif r < 20 and r > 10:
        y[0] = 3
        y[1] = 2
    elif r < 30 and r > 20:
        y[0] = 2
        y[1] = 1
    elif r < 40 and r > 30:
        y[0] = 1
        y[1] = 0
    draw()
    time.sleep(0.1)


