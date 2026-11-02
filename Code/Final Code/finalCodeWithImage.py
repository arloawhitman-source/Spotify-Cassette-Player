import time
import board
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_thinkink
import adafruit_requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_imageload import load

# wifi config
WIFI_SSID = "Your_WiFi_SSID"
WIFI_PASSWORD = "Your_WiFi_PASSWORD"

# airlift pins
spi = board.SPI()
esp32_cs = digitalio.DigitalInOut(board.D13)
esp32_ready = digitalio.DigitalInOut(board.D11)
esp32_reset = digitalio.DigitalInOut(board.D12)

esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

# Connect to Wi-Fi
print("Connecting to Wi-Fi...")
while not esp.is_connected:
    try:
        esp.connect_AP(WIFI_SSID, WIFI_PASSWORD)
    except Exception as e:
        print("Retrying connection...", e)
        time.sleep(1)
print("Connected to Wi-Fi!")

# Initialize Requests
socket.set_interface(esp)
requests = adafruit_requests.Session(socket)

# display init
display = adafruit_thinkink.Display(
    board.EPD_CS,
    board.EPD_DC,
    rst=board.RESET,
    busy=board.BUSY,
    ram_cs=None,
    highlight_color=adafruit_thinkink.YELLOW,
)

# display groups
splash = displayio.Group()
display.root_group = splash

SERVER_URL = "https://USERNAME_HERE.pythonanywhere.com/get-art" #Enter Your Username

def update_cassette_display():
    print("Fetching album art from server...")
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            # save bitmap
            with open("/temp_art.bmp", "wb") as f:
                f.write(response.content)
            
            # clear screen
            while len(splash) > 0:
                splash.pop()
                
            #load image on left side of screen
            bitmap, palette = load("/temp_art.bmp")
            tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
            splash.append(tile_grid)
            
            # Add text 
            track_label = label.Label(
                terminalio.FONT, text="Now Playing", color=0x000000, x=135, y=30
            )
            artist_label = label.Label(
                terminalio.FONT, text="Spotify Stream", color=0x000000, x=135, y=60
            )
            
            splash.append(track_label)
            splash.append(artist_label)
            
            # Refresh e-ink screen
            display.show()
            print("Screen updated successfully!")
        else:
            print("Server returned status code:", response.status_code)
    except Exception as e:
        print("Failed to update display:", e)

# check every 30 seconds
while True:
    update_cassette_display()
    time.sleep(30)