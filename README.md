# Car Game using Pygame

A fast-paced car dodging game built using **Python** and **Pygame**. The player controls a car on a highway, avoiding randomly appearing traffic. Survive as long as you can and aim for the highest score!


# About Game

  Car Game using Pygame is a simple yet addictive 2D racing-style game where the objective is to dodge incoming traffic for as long as possible. The player controls a car on a vertical scrolling highway, maneuvering between lanes to avoid collisions. Each obstacle (enemy vehicle) is randomly selected from a list of vehicle sprites and appears at different speeds and positions to keep the gameplay dynamic and challenging.
 
## 🎮 Gameplay Features

- 🏎️ **Player Car Movement**: Move left/right to switch lanes, and up/down to dodge traffic.
- 🧠 **Smart Obstacles**: Incoming cars appear in random lanes with randomized images.
- 🔥 **Collision Detection**: Blast animation and sound on collision.
- 📊 **Score System**: Score increases as you dodge vehicles.
- 🎵 **Background Music**: Plays during gameplay.
- 🎬 **Welcome + Game Over Screens**: Smooth transition between screens.

---

## 🕹️ Controls

- **Arrow Keys**:
  - Left / Right → Move car sideways
  - Up / Down → Move car forward/backward
- **SPACE** → Start or Restart game
- **ESC** → Quit game

---

## 📂 Project Structure

```
CarGame/
├── Game.py                 # Main game file
├── Gamesprites/               # All image/sound assets
│   ├── car.png
│   ├── highway.png
│   ├── redcar.png
│   ├── semi_trailer.png
│   ├── pickup_truck.png
│   ├── van.png
│   ├── blast.png
│   ├── gameover.png
│   ├── score.png
│   ├── Logo1.png
│   ├── logo2.png
│   └── [0-9].png              # Number images for score
├── backgroundsong.mp3
├── carblast.wav
└── README.md
```

## 💡 Future Ideas

- Add a pause/resume feature
- Difficulty scaling over time
- Powerups (like shields or slow-mo)
- Online high score leaderboard

---

## 🛠️ Installation process

Follow the steps below to set up and run the game on your machine:

### ✅ Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### 💾 Step-by-Step Guide

1. **Clone the Repository**

```bash
git clone https://github.com/PranitBijave27/2D_Car_Game-clone.git
cd car-game-pygame
```

2. **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install pygame
```

4. **Run the Game**

```bash
python Game.py
```

Make sure all image and sound assets are in the correct folders, as expected by the code.

---

## 👨‍💻 Author

**Pranit Bijave**  
GitHub -https://github.com/PranitBijave27


