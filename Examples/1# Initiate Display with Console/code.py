# Import the necessary modules
import displayio
import board
import busio
import adafruit_st7789

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

# Define the screen size and orientation
sX = 240 # Screen width in pixels
sY = 135 # Screen height in pixels

# Create the ST7789 display object
display = adafruit_st7789.ST7789(
    display_bus,            
    width=sX,
    height=sY,
    rowstart=40, # Offset from the top of the screen
    colstart=53, # Offset from the left of the screen
    rotation=90 # Rotate the screen by 90 degrees clockwise
)

# Print a welcome message to the console
print("Welcome!")
