import displayio
import board
import busio
import adafruit_st7789
import time
import adafruit_ds3231

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

# This line initializes the I2C bus using two GPIO pins on the board.
i2c = busio.I2C(board.GP3, board.GP2)

rtc = adafruit_ds3231.DS3231(i2c)

rtc.datetime = time.struct_time(time.localtime(time.time()))

while True:
    # Get the current date and time from the RTC.
    t = rtc.datetime
    
    # Print the date and time.
    print("{}/{}/{} {}:{:02}:{:02}".format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec))

    # Wait for a second before repeating.
    time.sleep(1)