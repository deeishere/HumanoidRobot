# HumanoidRobot 🤖

This project implements a simple command-line simulation of a humanoid robot.

---


## Used Hardware
- **ESP32** – Main microcontroller
- **TFT LCD 128x160** (x2) – Used for displaying the eyes and facial expressions
- **Speaker** – idk
- **Servo Motors** – For both shoulders
- **DC Motors** – For elbow movement
- **Distance Sensor** – To detect nearby presence (used to trigger waving)

---
## Used Libraries 
- Arduino Libraries for ESP32
`https://www.dropbox.com/scl/fo/ni8md8n1aha74t8wtgc7o/AL3rP5eLNBc1SCrsHDbVagk/Windows/Arduino_C/1.%20Get%20started%20with%20Arduino%20C%20before%20class/Arduino%20Libraries?dl=0&rlkey=2pyrlpnpicl60a3m5axjo6371`

- Speaker
`https://github.com/pschatzmann/ESP32-A2DP`


---
## Files
 ### 1. 🦾 Arms
- The **right arm** will automatically raise and wave if someone gets closer than **50 cm ** 

### 2. 👀 Eyes (Facial Expression System)
- The robot will display different **emotions** using virtual or LED-based eyes:
  - 😐 Normal
  - 😊 Happy
  - 🤩 Extremely Happy
  - 😠 Angry
  - 😢 Sad

### 3. 🔊 Speaker
- **TBA** – Will include voice responses or sound effects based on actions and interactions.

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. read requirement 
3. Clone the repo:
   ```bash
   git clone https://github.com/deeishere/HumanoidRobot.git
   cd HumanoidRobot
