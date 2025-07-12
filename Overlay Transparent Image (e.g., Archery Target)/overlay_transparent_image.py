import cv2
import sys
import numpy as np

# Function to overlay a transparent image
def overlay_transparent_image(background_path, overlay_path):
    try:
        # Load background and overlay images
        background = cv2.imread(background_path)
        overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)  # Load with alpha channel
        if background is None:
            raise FileNotFoundError(f"Error: Could not load background image at {background_path}.")
        if overlay is None:
            raise FileNotFoundError(f"Error: Could not load overlay image at {overlay_path}.")
        
        # Check if overlay has alpha channel
        if overlay.shape[2] != 4:
            raise ValueError("Error: Overlay image must have an alpha channel (e.g., PNG with transparency).")
        
        # Resize overlay to match background (optional, for simplicity)
        overlay = cv2.resize(overlay, (background.shape[1], background.shape[0]))
        
        # Split overlay into color and alpha channels
        overlay_color = overlay[:, :, :3]
        alpha_mask = overlay[:, :, 3] / 255.0
        
        # Create inverse alpha mask
        inverse_alpha = 1.0 - alpha_mask
        
        # Blend images
        for c in range(3):
            background[:, :, c] = (inverse_alpha * background[:, :, c] + alpha_mask * overlay_color[:, :, c]).astype(np.uint8)
        
        # Display the result
        cv2.imshow('Overlay Image', background)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save the result
        output_path = 'output_overlay.jpg'
        cv2.imwrite(output_path, background)
        print(f"Overlay image saved to {output_path}")
        
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
    if len(sys.argv) != 3:
        print("Usage: python overlay_transparent_image.py <background_path> <overlay_path>")
        sys.exit(1)
    background_path = sys.argv[1]
    overlay_path = sys.argv[2]
    overlay_transparent_image(background_path, overlay_path)