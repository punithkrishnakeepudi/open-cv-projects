# Convert to Grayscale Program

## Overview
This program converts an image to grayscale using `cv2.cvtColor()`. It displays and saves the grayscale image.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python convert_to_grayscale.py input.jpg
```
- Converts the image to grayscale.
- Displays and saves the result as `output_grayscale.jpg`.

## Code Explanation
- Loads an image with `cv2.imread()`.
- Converts to grayscale using `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`.
- Saves and displays the result.

## Error Handling
- Checks for valid image loading.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Fixed output path.
- No additional color space conversions.

## Troubleshooting
- **Image not loaded**: Verify file path.
- **Output not saved**: Check write permissions.

## Future Improvements
- Support other color space conversions.
- Allow user-defined output paths.