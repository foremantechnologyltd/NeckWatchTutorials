import displayio
import board
import busio
import adafruit_st7789
import time
import adafruit_ds3231
import terminalio
from adafruit_display_text import label # This class allows displaying text labels

# Release any previous displays
displayio.release_displays()

# Define the pins for the display
tft_cs = board.GP9 # Chip select pin
tft_dc = board.GP12 # Data/command pin
tft_res = board.GP13 # Reset pin
spi_mosi = board.GP11 # SPI MOSI pin
spi_clk = board.GP10 # SPI clock pin

# Initialize SPI and display bus
spi = busio.SPI(spi_clk, MOSI=spi_mosi)
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)

# This line initializes the I2C bus using two GPIO pins on the board.
i2c = busio.I2C(board.GP3, board.GP2)

rtc = adafruit_ds3231.DS3231(i2c)

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
text = "DATE" 
font = terminalio.FONT 
color = 0xFF00FF 
scale = 3

# Create a text label object with the specified attributes
text_date = label.Label(font, text=text, color=color, scale=scale)

# Set the position of the text label on the screen using percentages
text_date.x = x(15) 
text_date.y = y(35)

# Define the text, font, color and scale for the label
text = "TIME" 
font = terminalio.FONT 
color = 0x00FFFF 
scale = 4

# Create a text label object with the specified attributes
text_time = label.Label(font, text=text, color=color, scale=scale)

# Set the position of the text label on the screen using percentages
text_time.x = x(10) 
text_time.y = y(70)

group = displayio.Group()
group.append(text_time)
group.append(text_date)
# Show the text label on the display by adding it to the group
display.show(group)

rtc.datetime = time.struct_time((2023, 10, 9, 21, 38, 43, -1, -1, -1))

# Enter an infinite loop to keep the display active
while True:
    t = rtc.datetime
    text_date.text = "{}/{}/{}".format(t.tm_mday, t.tm_mon, t.tm_year)
    text_time.text = "{}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec)
    time.sleep(1)
