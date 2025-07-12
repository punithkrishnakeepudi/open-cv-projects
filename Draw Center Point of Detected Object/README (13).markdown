# Draw Center Point of Detected Object Program

## Overview
This program detects a red object and draws its center point using moments in a webcam feed.

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
python draw_center_point.py
```
- Draws center points of red objects.
- Displays the feed. Press 'q' to exit.

## Code Explanation
- Captures webcam feed.
- Applies red color mask in HSV.
- Finds contours and calculates centroids using moments.
- Draws center points.

## Error Handling
- Validates webcam and frame capture.
- Checks for valid moments.
- Ensures resource cleanup.

## Limitations
- Hardcoded red color range.
- Basic contour filtering.

## Troubleshooting
- **Webcam issues**: Check connection.
- **No centers drawn**: Adjust HSV range or object size.

## Future Improvements
- Support multiple colors.
- Save output video.