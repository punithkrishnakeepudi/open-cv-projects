import cv2
import sys

# Function to perform Canny edge detection
def canny_edge_detection(image_path):
    try:
        # Load the image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Apply Canny edge detection
        low_threshold = 100
        high_threshold = 200
        edges = cv2.Canny(image, low_threshold, high_threshold)
        
        # Display the edge-detected image
        cv2.imshow('Canny Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the edge-detected image
        output_path = 'output_canny.jpg'
        cv2.imwrite(output_path, edges)
        print(f"Edge-detected image saved to {output_path}")
        
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
    finally:
        cv2.destroyAllWindows()

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python edge_detection_canny.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    canny_edge_detection(image_path)