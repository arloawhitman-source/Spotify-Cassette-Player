import board
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_thinkink
import adafruit_portalbase.network
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi as ESP32SPI
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_imageload import load

#wifi configuration -change to match your wifi
Wifi_Ssid = "Your Wifi Ssid"
Wifi_Password = "Your Wifi Password"

#Spotify Auth -change for your token
Spotify_Access_Token = "Spotify Access Token

#Pins and Airlift init
spi = board.SPI()
esp32_cs = digitalio.DigitalInOut(board.D12)
esp32_ready = digitalio.DigitalInOUt(board.D11)
esp32_reset = digitalio.DigitalInOut(board.D13)

esp = ESP32SPI.ESP_SPI(spi, esp32_cs, esp32_ready, esp32_reset)

#Connect to wifi
print("Connecting to wifi")
while not esp.is_connected:
    try:
        esp.connect_AP(Wifi_Ssid, Wifi_Password)
    except Exception as e:
        print("Failed to connect, retrying asap", e)
        time.sleep(5)
print("Connected to", str(esp.ssid, "utf-8"))

#display init 
display = adafruit_thinkink.Display(
    spi,
    cs_pin = board.EPD_CS,
    dc_pin = board.EPD_DC
    busy_pin = board.EPD_BUSY,
    rst_pin = board.EPD_RESET,
    highlight_color = 0xff0000,
)

#display group
splash = displayio.Group()
display.root_group = splash

#set up text
track_label = label.Label(
    terminalio.FONT, text = "Waiting For Song", color = 0x000000, x = 10, y = 20
)
artist_label = label.Label(
    terminalio.FONT, text = "", color = 0x000000, x = 10, y = 40
)
album_label = label.Label(
    terminalio.FONT, text = "", color = 0x000000, x = 10, y = 60
)

splash.append(track_label)
splash.append(artist_label)
splash.append(album_label)

current_song_id = None
Spotify_Api_Url = "https://api.spotify.com/v1/me/player/currently-playing"

while True:
    try:
        print("Getting spotify data")
        headers = {"Authorization": f"Bearer {Spotify_Access_TOken}"}
        
        if response.status_code == 200:
            data = response.json()
            if data and data.get("item"):
                item = data["item"]
                track_name = item["name"]
                artist_name = item["artists"][0]["name"]
                album_name = item["album"]["name"]
                song_id = item["id"]
                
                #get low res cover image
                images = item["album"]["images"]
                album_cover_url = images[-1]["url"] if images else None
                
                if song_id != current_song_id:
                    current_song_id = song_id
                    print(f"Now Playing: {track_name} by {artist_name}")
                    
                    #update text
                    track_label.text = f"Track: {track_name[:20]}"
                    artist_label.text = f"Artist: {artist_name[:20]}"
                    album_label.text = f"Album: {album_name[:20]}"
                    
                    display.refresh()
            else:
                print("No song playing")
        elif response.status_code == 401:
            print("Token expired. Please generate a new access token.")
        else:
            print(f"API Error: {response.status_code}")
    except Exceptionas e:
        print(f"Error connecting to API: {e}")
    
    #delay between checks
    time.sleep(10)
