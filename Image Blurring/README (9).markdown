# Image Blurring Program

## Overview
This program applies Gaussian and simple blurring to an image using `cv2.GaussianBlur()` and `cv2.blur()`. It displays and saves both results.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python image_blurring.py input.jpg
```
- Applies Gaussian and simple blur.
- Displays and saves results as `output_gaussian_blur.jpg` and `output_simple_blur.jpg`.

## Code Explanation
- Loads an image.
- Applies `cv2.GaussianBlur()` and `cv2.blur()` with 5x5 kernels.
- Displays and saves results.

## Error Handling
- Validates image loading.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Hardcoded kernel size (5x5).
- Fixed output paths.

## Troubleshooting
- **Image not loaded**: Check file path.
- **Blur not effective**: Adjust kernel size.

## Future Improvements
- Allow user-defined kernel sizes.
- Support other blur types (e.g., median).