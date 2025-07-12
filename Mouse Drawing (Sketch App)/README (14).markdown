# Mouse Drawing (Sketch App) Program

## Overview
This program creates a simple sketch app allowing users to draw on a blank canvas using mouse events.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV and NumPy: `pip install opencv-python numpy`

## Usage
```bash
python mouse_drawing.py
```
- Click and drag to draw red lines.
- Press 'q' to save and exit.

## Code Explanation
- Creates a white 512x512 canvas.
- Uses `cv2.setMouseCallback()` to handle mouse events.
- Draws lines on mouse drag.
- Saves the drawing.

## Error Handling
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Fixed canvas size and color.
- Single color (red) for drawing.

## Troubleshooting
- **No drawing**: Ensure mouse events are detected.
- **Window not responding**: Check OpenCV GUI support.

## Future Improvements
- Add color and thickness options.
- Support erasing or undoing.