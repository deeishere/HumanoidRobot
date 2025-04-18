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

## Files
 ### 1. 🦾 Arms
- The **right arm** will automatically raise and wave if someone gets closer than **10 cm** 

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
