import cv2
import sys
import numpy as np

# Function to crop a region of interest (ROI)
def crop_roi(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Define ROI coordinates (example: top-left 100,100, width=200, height=200)
        x, y, w, h = 100, 100, 200, 200
        if x + w > image.shape[1] or y + h > image.shape[0]:
            raise ValueError("Error: ROI dimensions exceed image boundaries.")
        
        # Crop the ROI using NumPy slicing
        roi = image[y:y+h, x:x+w]
        
        # Display the ROI
        cv2.imshow('Region of Interest', roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the cropped image
        output_path = 'output_roi.jpg'
        cv2.imwrite(output_path, roi)
        print(f"Cropped ROI saved to {output_path}")
        
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
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
        print("Usage: python roi_cropping.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    crop_roi(image_path)