import cv2
import sys
import numpy as np

# Global variables for drawing
drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(img, (ix, iy), (x, y), (0, 0, 255), 2)
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Function to create a drawing app
def mouse_drawing():
    global img
    try:
        # Create a blank white image
        img = np.ones((512, 512, 3), np.uint8) * 255
        
        # Create a window and set mouse callback
        cv2.namedWindow('Drawing App')
        cv2.setMouseCallback('Drawing App', draw_circle)
        
        while True:
            cv2.imshow('Drawing App', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Save the drawing
        cv2.imwrite('output_drawing.jpg', img)
        print("Drawing saved to output_drawing.jpg")
        
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
    finally:
        cv2.destroyAllWindows()

# Main execution block
if __name__ == "__main__":
    mouse_drawing()