import cv2
import sys

# Function to detect faces in a webcam feed
def face_detection(haar_path):
    try:
        # Load Haar cascade classifier
        face_cascade = cv2.CascadeClassifier(haar_path)
        if face_cascade.empty():
            raise FileNotFoundError(f"Error: Could not load Haar cascade file at {haar_path}.")
        
        # Initialize webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Error: Could not open webcam.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                raise RuntimeError("Error: Failed to capture frame.")
            
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Display the frame
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
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
    if len(sys.argv) != 2:
        print("Usage: python face_detection_haar.py <haar_cascade_path>")
        sys.exit(1)
    haar_path = sys.argv[1]
    face_detection(haar_path)