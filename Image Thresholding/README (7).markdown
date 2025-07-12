# Image Thresholding Program

## Overview
This program applies binary thresholding to a grayscale image using `cv2.threshold()`. It converts pixel values above a threshold to white and below to black.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python image_thresholding.py input.jpg
```
- Applies binary thresholding.
- Displays and saves the result as `output_threshold.jpg`.

## Code Explanation
- Loads image in grayscale with `cv2.imread(..., cv2.IMREAD_GRAYSCALE)`.
- Applies `cv2.threshold()` with a threshold of 127.
- Saves and displays the result.

## Error Handling
- Validates image loading.
- Checks thresholding success.
- Ensures window closure.

## Limitations
- Hardcoded threshold value (127).
- Fixed output path.

## Troubleshooting
- **Image not loaded**: Check file path.
- **Thresholding fails**: Ensure image is valid.

## Future Improvements
- Allow user-defined threshold values.
- Support other thresholding types.