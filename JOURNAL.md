Title: Spotify Cassette Player

Github: https://github.com/arloawhitman-source/Spotify-Cassette-Player

Description: A small display to show current song on spotify as well as control spotify via the device.

Created_at: 2026-10-26

total_time: 10.5h


## October 26, 2026: Creating A PCB And Model For The Board

I used Kicad to create a schematic for the pcb that will hold four angled buttons as well as the Adafruit RP2040 Feather ThinkInk. I routed the PCB as well finally I assigned the 3d models of my components to have a model board to work on when designing the case. I also submitted a request for an acurate model of the e-ink display to have ready for modeling, if I cant get my hands on it i will use the provided schematics to make the case.

<img width="695" height="437" alt="Screenshot 2026-10-26 163029" src="https://github.com/user-attachments/assets/77d95117-224d-4921-8ce8-21b1568fbd84" />
<img width="1078" height="699" alt="Screenshot 2026-10-26 163017" src="https://github.com/user-attachments/assets/cee466b2-3442-43d0-a26b-abc828308a11" />


**Total time spent: 2h**



## October 27, 2026: Making A Case For The Board And Screen

I used Fusion to create the bottom of the Cassette case, I also hand modeled a model for the E-ink display. That was fairly easy due to it basically being a flat rectangle, however I also ended up doing more research and designing into how I wanted my keys. This allowed me to come up with a T shape to keep them from popping off the model. Im also slowly working on making the case look good. Finally I also had to decide things like wall depth and size of the overall model.

<img width="1047" height="492" alt="Screenshot 2026-10-27 171759" src="https://github.com/user-attachments/assets/cdd1f2df-742b-43fb-bb66-35fbdb720e77" />

**Total time spent: 2h**



## October 28, 2026: Finishing The Case 

I used fusion to finish the bottom half of the case as well as create the top half, I then tested all my components inside of the case to ensure they will fit. I still have to design my 3d printed buttons but once I do that I should be into programming of the board. Ive also decided to use glue to close the case as it will be the most secure. I might add latches later on in the process.

<img width="677" height="298" alt="Screenshot 2026-10-28 180029" src="https://github.com/user-attachments/assets/b9c854e6-7257-4a4e-a1d4-219c38962c25" />
<img width="913" height="538" alt="Screenshot 2026-10-28 180012" src="https://github.com/user-attachments/assets/c31a0956-0b57-43dc-b2ee-df1bc3a31a4f" />


**Total time spent: 3h**


## October 30, 2026: Finishing The Case And Ensuring Fit

I finished the case and designed the buttons, I modified the case slightly to allow the buttons to fit, I then put all of the parts in one model to ensure they would fit and check tolerances in my design. I then fixed small issues with the buttons sizing as well as the sizing around the screen. I can now move on to coding for my project

<img width="979" height="538" alt="Screenshot 2026-10-30 165323" src="https://github.com/user-attachments/assets/02a84b89-2beb-47a3-9412-053d913b13e5" />


**Total time spent: 1h**


## October 31, 2026: Programming with the spotify API

Happy Halloween ;)
I started programming the features needed to get the data from spotify, this was going well and was fairly simple, I watched a few tutorials before programming only the spotify features, my original plan was to have this plugged into my pc and transfer the data from it, however around two hours into coding this I realized that i would have to download every album cover on my pc and then send it over to the microcontroller, I didn't want to do this so I decided that I would add a wifi chip to my pcb design so it can all run from the board its self. I still attatched the inprogress files before using on board wifi.


<img width="1838" height="922" alt="coding" src="https://github.com/user-attachments/assets/f85e18e3-01de-44cf-a71d-040f4a20ac70" />


**Total time spent: 2h**



## November 1, 2026: Programming for the Airlift wifi card

As mentioned yesterday i've decided to add an arduino airlift to my design so it can access wifi to directly get data from spotify. I firsted programmed a simple program taking parts of yesterdays to display data from spotify such as artist, song and album, and this will be attatched once i'm able to get back to my normal pc. Ive also added a program thats hosted on pythonanywhere to get and compress the album cover art, this is slightly more complicated and required a different display script to be able to run. I did alot of debugging on the host site to get it to work but in a quick test the site is downloading a low res image of the album cover.

<img width="1245" height="495" alt="Screenshot_2026-11-01_15-14-58" src="https://github.com/user-attachments/assets/97307913-d40c-404a-96d8-072cb6bf5e79" />
<img width="1737" height="917" alt="Screenshot_2026-11-01_15-14-20" src="https://github.com/user-attachments/assets/78624c23-42dd-4b4e-a603-b4b6bc73c4f7" />

**Total time spent: 2.5h**


## November 2, 2026: Update CAD PCB and ReadMe

I updated the cad to include the new AirLift to support wifi, to do this I added onto the pcb with simple 1x12 pins. This didn't effect the CAD much as it still fit inside my case, however I did update the model a little bit to ensure it would fit snug and the buttons would actually work. Finally I updated the ReadMe to fit the requirements as well as the BOM to include the AirLift.

<img width="767" height="450" alt="Screenshot 2026-11-02 154055" src="https://github.com/user-attachments/assets/0dba12a4-84f1-4d93-8446-a7171dfccffe" />

**Total time spent: 1.8h**
