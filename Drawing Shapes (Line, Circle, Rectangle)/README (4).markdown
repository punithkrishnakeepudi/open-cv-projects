# Drawing Shapes Program

## Overview
This program uses OpenCV to draw a line, circle, and rectangle on an input image using `cv2.line()`, `cv2.circle()`, and `cv2.rectangle()`. It displays and saves the modified image.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file (e.g., `.jpg`, `.png`)

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python draw_shapes.py input.jpg
```
- Draws a red line, green circle, and blue rectangle on the image.
- Displays the result and saves it as `output_shapes.jpg`.

## Code Explanation
- Loads an image with `cv2.imread()`.
- Creates a copy to avoid modifying the original.
- Draws shapes with specified coordinates, colors (BGR), and thicknesses.
- Saves and displays the result.

## Error Handling
- Checks for invalid image paths or formats.
- Catches unexpected errors (e.g., memory issues).
- Ensures windows are closed in `finally`.

## Limitations
- Hardcoded shape parameters (coordinates, colors).
- Saves to a fixed output path (`output_shapes.jpg`).

## Troubleshooting
- **Image not loaded**: Verify file path and format.
- **Output not saved**: Check write permissions.

## Future Improvements
- Allow user-defined shape parameters via arguments.
- Support multiple shapes or colors.