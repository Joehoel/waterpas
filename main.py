from time import sleep

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

red = [240, 24, 24]
bubble = [136, 0, 120]

max_range = 600

number_of_pixels = 8

x_is_0 = False


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def reverseNumber(num, min, max):
    return (max + min) - num


def draw_axis(current, axis, x_is_0):
    if current >= max_range:
        current = max_range
    if current <= -max_range:
        current = -max_range

    range_per_pixel = (max_range * 2) / number_of_pixels
    pixel_light_up = round(current / range_per_pixel, 0)
    new_pixel_light_up = remap(pixel_light_up, -4, 4, 0, number_of_pixels)
    center = number_of_pixels / 2

    new_pixel_light_up = reverseNumber(new_pixel_light_up, 0, 8)

    for number in range(0, 8):
        skip = False

        if number == new_pixel_light_up or number == 7 and new_pixel_light_up == 8:
            if new_pixel_light_up == center:
                if axis == "x":
                    if number == 0:
                        x_is_0 = True
                    else:
                        x_is_0 = False

                    sense.set_pixel(number, 0, bubble)
                    sense.set_pixel(number - 1, 0, bubble)
                if axis == "y":
                    sense.set_pixel(0, number, bubble)
                    sense.set_pixel(0, number - 1, bubble)
            else:
                if axis == "x":
                    sense.set_pixel(number, 0, bubble)
                if axis == "y":
                    sense.set_pixel(0, number, bubble)
        else:
            if axis == "x":
                sense.set_pixel(number, 0, red)
            if axis == "y":
                if x_is_0 is False and number != 0:
                    sense.set_pixel(0, number, red)


try:
    while True:
        orientation_rad = sense.get_accelerometer_raw()
        draw_axis(orientation_rad["x"] * 1000, "x", x_is_0)
        draw_axis(orientation_rad["y"] * 1000, "y", x_is_0)
        sleep(0.1)
except KeyboardInterrupt:
    print("Program Shutdown")
