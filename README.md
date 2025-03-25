
# Virtual Mouse Using Hand Gestures

A Python-based virtual mouse system that allows users to control the computer mouse using hand gestures detected through a webcam, powered by **OpenCV**, **Mediapipe**, and **PyAutoGUI**.

## Features
- **Cursor Control**: Move your mouse pointer using your index finger.
- **Click Detection**: Perform mouse clicks by joining index and middle fingers.
- **Smooth Movement**: Built-in cursor movement smoothing to avoid jitter.
- **Scrolling Control**: Scroll up and down using specific finger combinations.
- **Hand Tracking**: Real-time tracking using Google's Mediapipe.

## Tech Stack
- Python
- OpenCV
- Mediapipe
- PyAutoGUI
- NumPy

## Requirements
- Python 3.7 to 3.11
- Webcam
- Libraries:
  - opencv-python
  - mediapipe
  - pyautogui
  - numpy

> Install dependencies easily:
```
pip install -r requirements.txt
```

## How to Run
1. Clone this repository or download the ZIP.
2. Install the required libraries using the above command.
3. Run the project:
```
python virtual_mouse_with_scroll.py
```
4. Show your hand gestures in front of your webcam to control the mouse.
5. Press **Q** to exit.
 

## License
This project is licensed under the MIT License — feel free to use, modify, and share.
