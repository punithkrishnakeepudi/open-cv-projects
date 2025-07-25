import cv2
import sys

# Function to convert an image to grayscale
def convert_to_grayscale(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Display the grayscale image
        cv2.imshow('Grayscale Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the grayscale image
        output_path = 'output_grayscale.jpg'
        cv2.imwrite(output_path, gray_image)
        print(f"Grayscale image saved to {output_path}")
        
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
        print("Usage: python convert_to_grayscale.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    convert_to_grayscale(image_path)