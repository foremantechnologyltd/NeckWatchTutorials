# Import the necessary modules
import displayio # This module provides classes to manage display devices
import board # This module provides access to the hardware pins on the board
import busio # This module provides classes for communication protocols
import adafruit_st7789 # This module provides a driver for the ST7789 TFT LCD display
import terminalio # This module provides a built-in font and terminal emulation
from adafruit_display_text import label # This class allows displaying text labels

# Release any previous displays
displayio.release_displays()

# Define the pins for the display and SPI communication
tft_cs = board.GP9 # Chip select pin
tft_dc = board.GP12 # Data/command pin
tft_res = board.GP13 # Reset pin
spi_mosi = board.GP11 # SPI MOSI pin
spi_clk = board.GP10 # SPI clock pin

# Initialize SPI and display bus
spi = busio.SPI(spi_clk, MOSI=spi_mosi) # Create a SPI object with the specified pins
display_bus = displayio.FourWire( # Create a FourWire object to communicate with the display
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)

# Define the screen size and orientation
sX = 240 # Screen width in pixels
sY = 135 # Screen height in pixels

# Create the ST7789 display object with the given parameters
display = adafruit_st7789.ST7789( # Initialize the display with the specified parameters
    display_bus,            
    width=sX,
    height=sY,
    rowstart=40, # Offset from the top of the screen
    colstart=53, # Offset from the left of the screen
    rotation=90 # Rotate the screen by 90 degrees clockwise
)

# Define functions to scale values from 0-100 to screen dimensions
def x(n): # Define a function to convert a percentage value to a pixel value along the x-axis
    p = sX / 100 # Calculate the pixel value of one percent of the screen width
    out = n * p # Multiply the percentage by the pixel value
    return int(out) # Return the result as an integer

def y(n): # Define a function to convert a percentage value to a pixel value along the y-axis
    p = sY / 100 # Calculate the pixel value of one percent of the screen height
    out = n * p # Multiply the percentage by the pixel value
    return int(out) # Return the result as an integer

# Create a display group to hold shapes and text labels
splash = displayio.Group()
display.show(splash)

# Define the text, font, color and scale for the label
text = "HELLO WORLD" 
font = terminalio.FONT 
color = 0xFF00FF 
scale = 3 

# Create a text label object with the specified attributes
text_area = label.Label(font, text=text, color=color, scale=scale)

# Set the position of the text label on the screen using percentages
text_area.x = x(10) 
text_area.y = y(50)

# Show the text label on the display by adding it to the group
display.show(text_area)

# Enter an infinite loop to keep the display active
while True:
    pass

