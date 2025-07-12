# Track Object with Color Program

## Overview
This program tracks a red object (e.g., a ball) in a webcam feed using HSV color masking and contour detection.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- Webcam

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV and NumPy: `pip install opencv-python numpy`

## Usage
```bash
python track_color_object.py
```
- Tracks red objects in the webcam feed.
- Displays the feed and mask. Press 'q' to exit.

## Code Explanation
- Captures webcam feed.
- Converts frames to HSV and applies red color mask.
- Finds and draws contours of red objects.
- Displays results.

## Error Handling
- Validates webcam and frame capture.
- Catches unexpected errors.
- Ensures resource cleanup.

## Limitations
- Hardcoded red color range.
- Basic contour filtering.

## Troubleshooting
- **Webcam not opened**: Check connection.
- **No objects detected**: Adjust HSV range or lighting.

## Future Improvements
- Allow user-defined color ranges.
- Save tracked video.