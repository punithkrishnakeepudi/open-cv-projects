# Face Detection with Haar Cascades Program

## Overview
This program detects faces in a webcam feed using OpenCV’s Haar cascade classifier.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- Webcam
- Haar cascade XML file (e.g., `haarcascade_frontalface_default.xml` from OpenCV’s GitHub)

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`
3. Download Haar cascade file from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage
```bash
python face_detection_haar.py haarcascade_frontalface_default.xml
```
- Detects faces and draws rectangles.
- Displays feed. Press 'q' to exit.

## Code Explanation
- Loads Haar cascade classifier.
- Captures webcam feed and converts to grayscale.
- Detects faces with `detectMultiScale()`.
- Draws rectangles around faces.

## Error Handling
- Validates Haar file and webcam.
- Checks frame capture.
- Ensures resource cleanup.

## Limitations
- Requires specific Haar cascade file.
- Basic face detection parameters.

## Troubleshooting
- **Haar file error**: Verify file path.
- **No faces detected**: Adjust `scaleFactor` or `minNeighbors`.

## Future Improvements
- Support multiple cascade types.
- Save detected faces.