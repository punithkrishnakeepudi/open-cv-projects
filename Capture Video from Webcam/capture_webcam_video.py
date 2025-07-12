import cv2
import sys

# Function to capture and display video from webcam
def capture_webcam_video():
    try:
        # Initialize video capture from default webcam (index 0)
        cap = cv2.VideoCapture(0)
        
        # Check if the webcam opened successfully
        if not cap.isOpened():
            raise RuntimeError("Error: Could not open webcam. Ensure it is connected and not in use by another application.")
        
        # Main loop to capture and display video frames
        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()
            
            # Check if frame was captured successfully
            if not ret:
                raise RuntimeError("Error: Failed to capture frame from webcam.")
            
            # Display the frame in a window
            cv2.imshow('Webcam Feed', frame)
            
            # Check for 'q' key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
        
    except RuntimeError as e:
        # Handle webcam or frame capture errors
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
    # Call the function to capture and display webcam video
    capture_webcam_video()