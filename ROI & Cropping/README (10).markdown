# ROI & Cropping Program

## Overview
This program crops a region of interest (ROI) from an image using NumPy array slicing. It displays and saves the cropped region.

## Prerequisites
- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- An image file

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV and NumPy: `pip install opencv-python numpy`

## Usage
```bash
python roi_cropping.py input.jpg
```
- Crops a 200x200 region from (100,100).
- Displays and saves the result as `output_roi.jpg`.

## Code Explanation
- Loads an image.
- Defines ROI coordinates and validates against image size.
- Crops using NumPy slicing (`image[y:y+h, x:x+w]`).
- Saves and displays the result.

## Error Handling
- Validates image loading and ROI dimensions.
- Catches unexpected errors.
- Ensures window closure.

## Limitations
- Hardcoded ROI coordinates.
- Fixed output path.

## Troubleshooting
- **Image not loaded**: Check file path.
- **ROI error**: Ensure coordinates fit image size.

## Future Improvements
- Allow user-defined ROI coordinates.
- Support multiple ROIs.