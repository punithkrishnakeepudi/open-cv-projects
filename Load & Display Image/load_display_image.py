import cv2
import sys

# Function to load and display an image
def load_and_display_image(image_path):
    try:
        # Load the image from the specified path
        image = cv2.imread(image_path)
        
        # Check if the image was successfully loaded
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}. Check if the file exists or is in a supported format (e.g., .jpg, .png).")
        
        # Display the image in a window
        cv2.imshow('Loaded Image', image)
        
        # Wait for a key press to close the window (0 means wait indefinitely)
        cv2.waitKey(0)
        
        # Close all OpenCV windows
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        # Handle file not found or invalid format errors
        print(e)
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

# Main execution block
if __name__ == "__main__":
    # Check if an image path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python load_display_image.py <image_path>")
        sys.exit(1)
    
    # Get the image path from command-line argument
    image_path = sys.argv[1]
    
    # Call the function to load and display the image
    load_and_display_image(image_path)