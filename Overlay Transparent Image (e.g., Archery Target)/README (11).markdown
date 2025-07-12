# Overlay Transparent Image Program

## Overview
This program overlays a transparent image (e.g., PNG with alpha channel) onto a background image using alpha blending.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- Background image and a transparent PNG (e.g., archery target)

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV and NumPy: `pip install opencv-python numpy`

## Usage
```bash
python overlay_transparent_image.py background.jpg overlay.png
```
- Overlays the transparent image on the background.
- Displays and saves the result as `output_overlay.jpg`.

## Code Explanation
- Loads background and overlay images (overlay with alpha channel).
- Resizes overlay to match background.
- Blends images using alpha mask.
- Saves and displays the result.

## Error Handling
- Validates image loading and alpha channel.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Assumes overlay matches background size after resizing.
- Fixed output path.

## Troubleshooting
- **Image not loaded**: Check file paths.
- **No alpha channel**: Use a PNG with transparency.

## Future Improvements
- Allow positioning the overlay.
- Support partial transparency adjustments.