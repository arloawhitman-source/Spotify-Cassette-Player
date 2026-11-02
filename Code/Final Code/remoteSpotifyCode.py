import io
from flask import Flask, send_file
from PIL import Image
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# spotify log in -change all three
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "https://your-server-name.pythonanywhere.com/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-read-playback-state",
        cache_path=".cache",  
    )
)


@app.route("/get-art")
def get_album_art():
  try:
    # get song on spotify
    playback = sp.current_user_playing_track()

    if playback and playback["item"]:
      # get image URL
      album_cover_url = playback["item"]["album"]["images"][0]["url"]

      # Download image
      img_response = requests.get(album_cover_url)
      if img_response.status_code == 200:
        # open with pillow
        img = Image.open(io.BytesIO(img_response.content))

        # resize to match screen
        img = img.resize((80, 80))

        # change to quad color
        palette_data = [
            0, 0, 0,        # 0: Black
            255, 255, 255,  # 1: White
            255, 0, 0,      # 2: Red
            255, 255, 0,    # 3: Yellow
        ]
       
        palette_data += [0] * (768 - len(palette_data))

        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette(palette_data)

        # convert to rgb
        img = img.convert("RGB")
        img = img.quantize(palette=pal_img, dither=Image.Dither.FLOYDSTEINBERG)

        # save as bmp
        output = io.BytesIO()
        img.save(output, format="BMP")
        output.seek(0)

        #send to board
        return send_file(output, mimetype="image/bmp")

    
    return "No song playing", 404

  except Exception as e:
    return str(e), 500


if __name__ == "__main__":
  app.run(debug=True)