import cv2
import sys
import os

# Function to capture a video frame and save it
def save_frame_from_video(save_path):
    try:
        # Initialize video capture from default webcam (index 0)
        cap = cv2.VideoCapture(0)
        
        # Check if the webcam opened successfully
        if not cap.isOpened():
            raise RuntimeError("Error: Could not open webcam. Ensure it is connected and not in use by another application.")
        
        # Read a single frame from the webcam
        ret, frame = cap.read()
        
        # Check if frame was captured successfully
        if not ret:
            raise RuntimeError("Error: Failed to capture frame from webcam.")
        
        # Check if the save path is valid and has a supported extension
        valid_extensions = ['.jpg', '.png', '.jpeg']
        if not os.path.splitext(save_path)[1].lower() in valid_extensions:
            raise ValueError(f"Error: Invalid file extension for {save_path}. Use .jpg, .png, or .jpeg.")
        
        # Save the captured frame to the specified path
        cv2.imwrite(save_path, frame)
        print(f"Frame saved successfully to {save_path}")
        
        # Display the captured frame for confirmation
        cv2.imshow('Captured Frame', frame)
        cv2.waitKey(0)  # Wait for any key press to close the window
        
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
        
    except RuntimeError as e:
        # Handle webcam or frame capture errors
        print(e)
        sys.exit(1)
    except ValueError as e:
        # Handle invalid file extension errors
        print(e)
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
    finally:
        # Ensure resources are released even if an error occurs
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()

# Main execution block
if __name__ == "__main__":
    # Check if a save path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python save_frame_from_video.py <save_path>")
        sys.exit(1)
    
    # Get the save path from command-line argument
    save_path = sys.argv[1]
    
    # Call the function to capture and save a frame
    save_frame_from_video(save_path)