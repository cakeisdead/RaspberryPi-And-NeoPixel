import time
import board
import neopixel

# NeoPixel parameters
LED_COUNT = 32 # Number of LED pixels - The FeatherWing has 32 leds
DATA_PIN = board.D18 # GPIO PI - We are using GPIO 18 to communicate with the FeatherWing
LED_BRIGHTNESS = 1  # 1 is REALLY bright
AW = False      # auto_write
COLOR_ORDER = neopixel.RGB # this is the color channel order. (GRB, GRBW, RGB or RGBW)

# Color Settings (RGB values)
color_none = (0,0,0)
color_moving = (6,245,42)
color_final = (235,106,71)

# Create NeoPixel object with appropriate configuration.
fw = neopixel.NeoPixel(DATA_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=AW, pixel_order = COLOR_ORDER)


def putPixel(position, color):
    fw[position] = color
    fw.show()

final = LED_COUNT

while final >= 0:
    for led in range(final):
        putPixel(led,color_moving)
        time.sleep(0.1)
        putPixel(led,color_none)
    putPixel(final-1, color_final)
    final -= 1
