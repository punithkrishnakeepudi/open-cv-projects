import cv2
import sys
import numpy as np

# Function to draw shapes on an image
def draw_shapes(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}. Check file path and format.")
        
        # Create a copy to draw shapes
        img_copy = image.copy()
        
        # Draw a line (red, thickness=2)
        cv2.line(img_copy, (50, 50), (200, 50), (0, 0, 255), 2)
        
        # Draw a circle (green, thickness=3)
        cv2.circle(img_copy, (150, 150), 50, (0, 255, 0), 3)
        
        # Draw a rectangle (blue, thickness=2)
        cv2.rectangle(img_copy, (100, 200), (200, 300), (255, 0, 0), 2)
        
        # Display the image with shapes
        cv2.imshow('Image with Shapes', img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the modified image
        output_path = 'output_shapes.jpg'
        cv2.imwrite(output_path, img_copy)
        print(f"Image with shapes saved to {output_path}")
        
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
        print("Usage: python draw_shapes.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    draw_shapes(image_path)