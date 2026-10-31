import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial

#Spotify Credentialls -update for your credentials
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id = "Client ID Here",
        client_secret = "Client Secret Here",
        redirect_uri = "http://127.0.0.1:8080/callback", #No need to change this :)
        scope = "user-read-playback-state",
    )
)

#Connect to tho the microcontroller -in the next line change COM3 to your actual port
ser = serial.Serial("COM3", 9600, timeout = 1)
time.sleep(2)

current_song_id = None

print("Starting Tracker Script")

while True:
    try:
        #Get info from spotify
        playback = sp.current_user_playing_track()
        
        #Set vars to the spotify info
        if playback and playback["item"]:
            track_name = playback["item"]["name"]
            artist_name = playback["item"]["artists"][0]["name"]
            album_name = playback["item"]["album"]["name"]
            song_id = playback["item"]["id"]
            album_cover_url = playback["item"]["album"]["images"][0]["url"] #O is the largest image
            
            if song_id != current_song_id:
                current_song_id = song_id
                print(f"now Playing: {track_name} by {artist_name}")
                print(f"Cover art url: {album_cover_url}")
                
                #format for sending to the board
                payload = f"{track_name}|{artist_name}|{album_name}|{album_covr_url}\n"
                
                #send to board
                ser.write(payload.encode("utf-8"))
                
        else:
            print("No Song Currently Playing.")
        
    except Exception as e:
        print(f"Error: {e}")
    
    #How long to wait before checking again
    time.sleep(5)
