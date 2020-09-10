from sense_hat import SenseHat
from sms import message
from db import insert
from threading import Timer
from inspect import signature
import time

sense = SenseHat()

WHITE = (0, 0, 255)

orientation  = 0
pitch = [0, 0]
roll = [0, 0]
p = 0
r = 0
x = [0, 0]
y = [0, 0]


def debounce(wait):
    def decorator(fn):
        sig = signature(fn)
        caller = {}

        def debounced(*args, **kwargs):
            nonlocal caller

            try:
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                called_args = fn.__name__ + str(dict(bound_args.arguments))
            except:
                called_args = ''

            t_ = time.time()

            def call_it(key):
                try:
                    # always remove on call
                    caller.pop(key)
                except:
                    pass

                fn(*args, **kwargs)

            try:
                # Always try to cancel timer
                caller[called_args].cancel()
            except:
                pass

            caller[called_args] = Timer(wait, call_it, [called_args])
            caller[called_args].start()

        return debounced

    return decorator

@debounce(1.5)
def pressed():
    message(f"Current postion: \nPitch: {p}\nRoll: {r}")
    insert(p,r)

# Draw the bubble on LED matrix
# def draw():
#     sense.set_pixel(x[0], y[0], WHITE)
#     sense.set_pixel(x[0], y[1], WHITE)
#     sense.set_pixel(x[1], y[0], WHITE)
#     sense.set_pixel(x[1], y[1], WHITE)

sense.stick.direction_any = pressed 
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
    p = round((pitch[0] + pitch[1]) / 2)
    r = round((roll[0] + roll[1]) / 2)
    print("pitch: ", p, "roll: ", r)
    
    sense.clear()
    if ((p < 10 and p > 0) or (p < 360 and p > 350) or (p == 0) or (p == 360)) and ((r < 10 and r > 0) or (r < 360 and r > 350) or (r == 0) or (r == 360)):
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
            
    sense.set_pixel(x[0], y[0], WHITE)
    sense.set_pixel(x[0], y[1], WHITE)
    sense.set_pixel(x[1], y[0], WHITE)
    sense.set_pixel(x[1], y[1], WHITE)
    
    time.sleep(0.1)


