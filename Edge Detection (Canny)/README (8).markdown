# Edge Detection (Canny) Program

## Overview
This program applies Canny edge detection using `cv2.Canny()` to a grayscale image, highlighting edges.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python edge_detection_canny.py input.jpg
```
- Detects edges using Canny algorithm.
- Displays and saves the result as `output_canny.jpg`.

## Code Explanation
- Loads image in grayscale.
- Applies `cv2.Canny()` with thresholds 100 and 200.
- Saves and displays the result.

## Error Handling
- Validates image loading.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Hardcoded threshold values.
- Fixed output path.

## Troubleshooting
- **Image not loaded**: Check file path.
- **Edges not clear**: Adjust threshold values.

## Future Improvements
- Allow user-defined thresholds.
- Add preprocessing (e.g., blurring).