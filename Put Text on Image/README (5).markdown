# Put Text on Image Program

## Overview
This program uses `cv2.putText()` to add text to an image with specified font style, size, and color. It displays and saves the modified image.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV: `pip install opencv-python`

## Usage
```bash
python put_text_on_image.py input.jpg
```
- Adds "Hello, OpenCV!" to the image.
- Displays and saves the result as `output_text.jpg`.

## Code Explanation
- Loads an image with `cv2.imread()`.
- Uses `cv2.putText()` with `font_HERSHEY_SIMPLEX`, scale, color, and thickness.
- Saves and displays the result.

## Error Handling
- Validates image loading.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Hardcoded text and parameters.
- Fixed output path.

## Troubleshooting
- **Image not loaded**: Check file path.
- **Text not visible**: Adjust coordinates or color for contrast.

## Future Improvements
- Allow user-defined text and font parameters.
- Support multiple text placements.