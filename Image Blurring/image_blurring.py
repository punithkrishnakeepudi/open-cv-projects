import cv2
import sys

# Function to apply blurring to an image
def apply_blurring(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Apply Gaussian blur
        gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
        
        # Apply simple blur
        simple_blur = cv2.blur(image, (5, 5))
        
        # Display original and blurred images
        cv2.imshow('Original Image', image)
        cv2.imshow('Gaussian Blur', gaussian_blur)
        cv2.imshow('Simple Blur', simple_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save blurred images
        cv2.imwrite('output_gaussian_blur.jpg', gaussian_blur)
        cv2.imwrite('output_simple_blur.jpg', simple_blur)
        print("Blurred images saved as output_gaussian_blur.jpg and output_simple_blur.jpg")
        
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
        print("Usage: python image_blurring.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    apply_blurring(image_path)