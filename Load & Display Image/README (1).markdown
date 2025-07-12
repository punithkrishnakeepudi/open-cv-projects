# Load & Display Image Program

## Overview
This Python program uses OpenCV to load an image from a specified file path and display it in a window. It introduces fundamental OpenCV functions: `cv2.imread()` for loading the image, `cv2.imshow()` for displaying it, and `cv2.waitKey()` for handling user input to close the window.

## Prerequisites
- **Python 3.x**: Ensure Python is installed.
- **OpenCV**: Install OpenCV using `pip install opencv-python`.
- **Image File**: Provide a valid image file (e.g., `.jpg`, `.png`) in a supported format.

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV:
   ```bash
   pip install opencv-python
   ```
3. Ensure you have an image file (e.g., `sample.jpg`) in your working directory or provide the full path.

## Usage
Run the program from the command line, providing the path to an image file:
```bash
python load_display_image.py sample.jpg
```
- The program loads the image and displays it in a window.
- Press any key to close the window.

## Code Explanation
- **Imports**:
  - `cv2`: OpenCV library for image processing.
  - `sys`: For handling command-line arguments and program exit.
- **Function `load_and_display_image(image_path)`**:
  - Uses `cv2.imread(image_path)` to load the image.
  - Checks if the image was loaded successfully (returns `None` if not).
  - Displays the image using `cv2.imshow('Loaded Image', image)`.
  - Uses `cv2.waitKey(0)` to wait for a key press.
  - Closes windows with `cv2.destroyAllWindows()`.
- **Main Block**:
  - Checks for a command-line argument (image path).
  - Calls the main function with the provided path.

## Error Handling
- **FileNotFoundError**: If the image file doesn’t exist or is in an unsupported format, the program prints an error message and exits.
- **General Exceptions**: Catches unexpected errors (e.g., corrupted image files) and exits with an error message.
- **Command-Line Argument Check**: Ensures exactly one argument (image path) is provided.

## Limitations
- Supports common image formats (e.g., `.jpg`, `.png`). Other formats may fail.
- The program assumes the image can fit in memory.
- No support for resizing or modifying the image in this basic version.

## Example
```bash
python load_display_image.py images/sample.jpg
```
- Loads `sample.jpg` from the `images` directory.
- Displays the image in a window.
- Closes the window when a key is pressed.

## Troubleshooting
- **Error: Could not load image**: Verify the file path and ensure the image is in a supported format.
- **No window appears**: Ensure OpenCV is installed correctly and your system supports GUI windows.
- **Program crashes**: Check for corrupted image files or insufficient memory.

## Future Improvements
- Add support for multiple image formats.
- Allow resizing the image before display.
- Add a GUI for selecting the image file.