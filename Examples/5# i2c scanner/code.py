import displayio
import board
import busio
import adafruit_st7789
import time

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

# This function scans the I2C bus for any connected devices.
def scan_i2c():
    # Print a message indicating the start of the scan.
    print("Scanning I2C bus...")
    # Scan the I2C bus and store any found device addresses in the 'devices' variable.
    devices = i2c.scan()
    # If no devices are found, print a message indicating this.
    if len(devices) == 0:
        print("No devices found")
    # If devices are found, print the number of devices and their addresses.
    else:
        print("Found %d device(s)" % len(devices))
        for device in devices:
            print("Device at address 0x%02X" % device)

# This loop attempts to lock the I2C bus. If it's already locked, it waits and tries again.
while not i2c.try_lock():
    pass

# This is the main loop of the program. It continuously scans the I2C bus every 5 seconds.
while True:
    scan_i2c()
    time.sleep(5)

