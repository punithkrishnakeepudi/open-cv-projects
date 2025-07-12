import cv2
import sys

# Function to apply binary thresholding to an image
def apply_thresholding(image_path):
    try:
        # Load the image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Apply binary thresholding
        thresh_value = 127
        max_value = 255
        ret, thresh_image = cv2.threshold(image, thresh_value, max_value, cv2.THRESH_BINARY)
        
        if ret is None:
            raise RuntimeError("Error: Thresholding failed.")
        
        # Display the thresholded image
        cv2.imshow('Thresholded Image', thresh_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the thresholded image
        output_path = 'output_threshold.jpg'
        cv2.imwrite(output_path, thresh_image)
        print(f"Thresholded image saved to {output_path}")
        
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
        cv2.destroyAllWindows()

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_thresholding.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    apply_thresholding(image_path)