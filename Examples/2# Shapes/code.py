# Import necessary libraries
import displayio # This module provides classes to manage display devices
import board # This module provides access to the hardware pins on the board
import busio # This module provides classes for communication protocols
import adafruit_st7789 # This module provides a driver for the ST7789 TFT LCD display
from adafruit_display_shapes.rect import Rect # This class allows drawing rectangles
from adafruit_display_shapes.circle import Circle # This class allows drawing circles
from adafruit_display_shapes.roundrect import RoundRect # This class allows drawing rounded rectangles

# Release any existing displays
displayio.release_displays()

# Define pin assignments for the display and SPI communication
tft_cs = board.GP9 # Chip select pin
tft_dc = board.GP12 # Data/command pin
tft_res = board.GP13 # Reset pin
spi_mosi = board.GP11 # SPI MOSI pin
spi_clk = board.GP10 # SPI clock pin

# Create an SPI bus
spi = busio.SPI(spi_clk, MOSI=spi_mosi)

# Create a display bus for the ST7789 display
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)

# Define the screen dimensions
sX = 240 # Screen width in pixels
sY = 135 # Screen height in pixels

# Create an ST7789 display object with specified parameters
display = adafruit_st7789.ST7789(
    display_bus,
    width=sX,
    height=sY,
    rowstart=40, # Offset from the top of the screen
    colstart=53, # Offset from the left of the screen
    rotation=90 # Rotate the screen by 90 degrees clockwise
)

# Define functions to scale values from 0-100 to screen dimensions
def x(n):
    p = sX / 100 # Calculate the pixel value of one percent of the screen width
    out = n * p # Multiply the percentage by the pixel value
    return int(out) # Return the result as an integer

def y(n):
    p = sY / 100 # Calculate the pixel value of one percent of the screen height
    out = n * p # Multiply the percentage by the pixel value
    return int(out) # Return the result as an integer

# Create a display group to hold shapes
splash = displayio.Group()
display.show(splash)

# Create various shapes and add them to the display group
rect = Rect(x(2), y(2), x(30), y(70), fill=0x00ff00) # Create a green rectangle with 30% width and 70% height at (2%, 2%) position 
splash.append(rect)

circle = Circle(x(45), y(25), x(10), fill=0x00FFFF, outline=0xFF00FF) # Create a cyan circle with magenta outline and 10% radius at (45%, 25%) position 
splash.append(circle)

rect2 = Rect(x(2), y(80), x(98), y(20), outline=0xff0000, stroke=3) # Create a red rectangle with 3 pixels stroke and no fill with 98% width and 20% height at (2%, 80%) position 
splash.append(rect2)

roundrect = RoundRect(150, 10, 61, 81, 10, fill=0xFFFF00, outline=0xFF00FF, stroke=6) # Create a yellow rounded rectangle with magenta outline and 6 pixels stroke with 61 pixels width and 81 pixels height and 10 pixels corner radius at (150, 10) position 
splash.append(roundrect)

# Enter an infinite loop to keep the display active
while True:
    pass