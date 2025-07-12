# Capture Video from Webcam Program

## Overview
This Python program uses OpenCV to capture and display a live video feed from the default webcam. It demonstrates the use of `cv2.VideoCapture()` for accessing the webcam and `cv2.imshow()` for displaying the video feed in real-time. The program exits when the user presses the 'q' key.

## Prerequisites
- **Python 3.x**: Ensure Python is installed.
- **OpenCV**: Install OpenCV using `pip install opencv-python`.
- **Webcam**: A working webcam connected to your computer (built-in or external).
- **Operating System**: Ensure your OS supports webcam access (Windows, macOS, or Linux).

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV:
   ```bash
   pip install opencv-python
   ```
3. Verify that your webcam is connected and functional (test with another application if needed).

## Usage
Run the program from the command line:
```bash
python capture_webcam_video.py
```
- The program opens a window displaying the live webcam feed.
- Press the 'q' key to exit the program and close the window.

## Code Explanation
- **Imports**:
  - `cv2`: OpenCV library for video capture and display.
  - `sys`: For program exit on errors.
- **Function `capture_webcam_video()`**:
  - Initializes `cv2.VideoCapture(0)` to access the default webcam (index 0).
  - Checks if the webcam opened successfully using `cap.isOpened()`.
  - Enters a loop to:
    - Capture frames with `cap.read()`, returning a boolean (`ret`) and the frame.
    - Display each frame using `cv2.imshow('Webcam Feed', frame)`.
    - Check for the 'q' key press with `cv2.waitKey(1)` to exit.
  - Releases the webcam with `cap.release()` and closes windows with `cv2.destroyAllWindows()`.
- **Error Handling**:
  - Checks for webcam access failure.
  - Validates frame capture success.
  - Uses a `finally` block to ensure resources are released.
- **Main Block**:
  - Calls the main function to start the webcam feed.

## Error Handling
- **RuntimeError**: Raised if the webcam cannot be opened (e.g., not connected, in use, or driver issues) or if frame capture fails.
- **General Exceptions**: Catches unexpected errors (e.g., hardware failures or memory issues).
- **Resource Cleanup**: The `finally` block ensures the webcam is released and windows are closed, preventing resource leaks.

## Limitations
- Uses the default webcam (index 0). To use a different webcam, modify the index in `cv2.VideoCapture()`.
- No frame rate or resolution adjustments are included in this basic version.
- Assumes the system supports GUI windows for `cv2.imshow()`.

## Example
```bash
python capture_webcam_video.py
```
- Opens a window showing the live webcam feed.
- Press 'q' to exit, closing the window.

## Troubleshooting
- **Error: Could not open webcam**: Ensure the webcam is connected, not in use by another application, and has proper drivers installed.
- **Error: Failed to capture frame**: Check webcam functionality or try restarting the program.
- **No window appears**: Verify OpenCV is installed correctly and your system supports GUI windows.
- **Program hangs on exit**: Ensure the `finally` block is executed to release resources.

## Future Improvements
- Add support for selecting different webcams (e.g., via command-line arguments).
- Allow adjusting frame rate or resolution.
- Save the video feed to a file (similar to Program 3 in your list).