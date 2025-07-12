import cv2
import sys
import numpy as np

# Function to track a red object in a webcam feed
def track_color_object():
    try:
        # Initialize webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Error: Could not open webcam.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                raise RuntimeError("Error: Failed to capture frame.")
            
            # Convert to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # Define range for red color
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)
            
            lower_red2 = np.array([170, 120, 70])
            upper_red2 = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
            mask = mask1 + mask2
            
            # Find contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Draw contours on frame
            for contour in contours:
                if cv2.contourArea(contour) > 500:  # Filter small contours
                    cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            
            # Display the frame and mask
            cv2.imshow('Webcam Feed', frame)
            cv2.imshow('Red Mask', mask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
    except RuntimeError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()

# Main execution block
if __name__ == "__main__":
    track_color_object()