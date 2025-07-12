import cv2
import sys

# Function to add text to an image
def put_text_on_image(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Could not load image at {image_path}.")
        
        # Define text parameters
        text = "Hello, OpenCV!"
        org = (50, 50)  # Bottom-left corner of text
        font = cv2.font_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)  # White text
        thickness = 2
        
        # Add text to the image
        image = cv2.putText(image, text, org, font, font_scale, color, thickness, cv2.LINE_AA)
        
        # Display the image
        cv2.imshow('Image with Text', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the modified image
        output_path = 'output_text.jpg'
        cv2.imwrite(output_path, image)
        print(f"Image with text saved to {output_path}")
        
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
        print("Usage: python put_text_on_image.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    put_text_on_image(image_path)