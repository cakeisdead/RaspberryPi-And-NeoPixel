import time
import board
import neopixel

# NeoPixel parameters
led_count = 32 # Number of LED pixels - The FeatherWing has 32 leds
data_pin = board.D18 # GPIO PI - We are using GPIO 18 to communicate with the FeatherWing
led_brightness = 1  # 1 is REALLY bright
aw = False      # auto_write
color_order = neopixel.RGB # this is the color channel order. (GRB, GRBW, RGB or RGBW)

# Color Settings (RGB values)
colorNone = (0,0,0)
colorMoving = (6,245,42)
colorFinal = (235,106,71)

# Create NeoPixel object with appropriate configuration.
fw = neopixel.NeoPixel(data_pin, led_count, brightness = led_brightness, auto_write=aw, pixel_order = color_order)


def putPixel(position, color):
    fw[position] = color
    fw.show()

final = LED_COUNT

while final >= 0:
    for led in range(final):
        putPixel(led,colorMoving)
        time.sleep(0.1)
        putPixel(led,colorNone)
    putPixel(final-1, colorFinal)
    final -= 1
