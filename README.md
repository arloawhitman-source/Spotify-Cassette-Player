# What Is Spotify Cassette Player?
I am making a spotify display which will show album covers, lyrics, and have audio control functionality. This is placed into a 3d printed case made to look like a cassette player. The project uses a small quad color e-ink display to display the information.

# Features
This project uses a small microcontroller especially made for e-ink displays, this is paired with a adafruit AirLift to make it work completely on its own. It also has a programable button for future expansion or ideas. It features three buttons for music control to be implemented which will happen after I ensure that the rest of the code works.

# Assembly
<img width="986" height="628" alt="Screenshot 2026-10-28 180455" src="https://github.com/user-attachments/assets/afec40ae-2527-4490-a66b-64a7469286af" />
<img width="951" height="671" alt="Screenshot 2026-10-28 181416" src="https://github.com/user-attachments/assets/12a5ac27-31e4-4ecb-b98f-4fff126d0b74" />

# Case
<img width="968" height="446" alt="Screenshot 2026-11-02 154927" src="https://github.com/user-attachments/assets/581b85b8-0db6-41bb-b0da-068930db12ae" />

# Wiring Diagram/PCB
<img width="767" height="450" alt="Screenshot 2026-11-02 154055" src="https://github.com/user-attachments/assets/d6b52191-8373-4fcf-a576-81d0096fe0d4" />
<img width="970" height="406" alt="Screenshot 2026-11-02 154100" src="https://github.com/user-attachments/assets/81234898-8735-4f8c-9b5b-eb7dfaa57fa9" />
<img width="927" height="477" alt="Screenshot 2026-11-02 154105" src="https://github.com/user-attachments/assets/222fdfc6-703f-480b-bbf8-d2a7eb455c0f" />

# Code
The code in this project is largely untested however this page will be updated with final code once I can test it. One of the biggest problems with using the RP2040 is that it has very little on board ram or memory, to download and scale down images I wrote a script to be hosted on pythonanywhere to communicate with your project. Again I will update this page with further instructions once I am able to test the communication between my project and the pythonanywhere site.

# Spotify For Developers
In order for this project to work you must first set up a spotify developer project. This is done by going to spotify for developers website and logging in to spotify like normal, next create a project and give it an appropriate name and description. Finally under the call backs add these two links: https://YOURUSERNAMEHERE.pythonanywhere.com/callback http://127.0.0.1:8080/callback Last save your project and ensure the callback links match the ones running on your project.
