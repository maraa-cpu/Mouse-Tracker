# Mouse Tracker

A lightweight and intuitive Python script that allows you to control your computer's cursor using hand movements via your webcam. 

This project leverages **MediaPipe** for hand landmark tracking, **OpenCV** for video processing, and **pynput** to translate digital coordinates into physical mouse actions.

## Features

* **Real-time Pointing:** Control the cursor by moving your index finger tip.
* **Click and Drag & Drop:** Bring your index finger and thumb tips together (pinch gesture) to simulate a left mouse click. Move them apart to release.
* **Intelligent Smoothing:** Implements a smoothing algorithm to eliminate jitter and ensure a professional pointing experience.
* **Visual Debugging:** The webcam window displays real-time tracking and a status indicator (Clicked/Free) for immediate feedback.

## Installation & Requirements

Ensure you have **Python 3.x** installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   cd REPO_NAME
   ```

2. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe pynput
   ```

## Usage

Run the script from your terminal:

```bash
python mouse.py
```

### Gesture Guide
* **Move Cursor:** Use the tip of your **index finger**.
* **Click / Drag:** Touch the tips of your **index finger and thumb** together (pinch).
* **Release:** Separate the fingers.
* **Exit:** Press the `ESC` key while the webcam window is focused.

## Important: macOS Setup

To allow the script to control the cursor on macOS, you must grant **Accessibility** permissions to your Terminal or IDE:

1. Open **System Settings** > **Privacy & Security** > **Accessibility**.
2. Toggle the switch **ON** for your Terminal (e.g., Terminal, iTerm2) or Code Editor (e.g., VS Code).

## Configuration

You can customize the following variables at the top of `mouse.py` to fit your setup:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `SMOOTHING` | `5` | Higher = smoother but slower; Lower = faster/snappier. |
| `CLICK_THRESHOLD` | `0.04` | Sensitivity of the pinch gesture. |
| `SCREEN_WIDTH` | `1920` | Set this to match your monitor's width. |
| `SCREEN_HEIGHT` | `1080` | Set this to match your monitor's height. |

## License
This project is open-source. Feel free to modify and share!
