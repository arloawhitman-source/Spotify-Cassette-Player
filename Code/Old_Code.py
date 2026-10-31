import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_thinkink

#initilize the board setup
display = adafruit_thinkink.Display(
    board.SPI(),
    cs_pin = board.D9
    dc_pin = board.D10,
    busy_pin = board.D5,
    rst_pin = board.D6
    highlight_color= 0xFF0000,
)

#Create group for text info
splash = displayio.Group()
display.root_group = splash

#set up text
track_label = label.Label(
    terminalio.FONT, text = "Waiting For Song...", color = 0x000000, x = 10, y = 20
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

print("Listening for data from pc")

while True:
    #check if the board is recieving data
    if supervisor.runtime.serial_bytes_available:
        line = input().strip() #read line
        
        if "|" in line:
            parts = line.split("|")
            if len(parts) >= 3:
                track_name = parts[0]
                artist_name = parts[1]
                album_name = parts[2]
                
                #update text
                track_label.text = f"Track: {track_name}"
                artist_label.text = f"Artist: {artist_name}"
                album_label.text = f"Album: {album_name}"
                
                display.refresh()
