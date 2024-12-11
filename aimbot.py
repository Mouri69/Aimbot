import pyautogui
import numpy as np
from PIL import ImageGrab
import keyboard
import time

# Function to check if a pixel is red
def is_red(pixel):
    r, g, b = pixel
    return r > 150 and g < 100 and b < 100  # Adjust thresholds as needed

# Function to find the nearest red pixel in a faster way (by sampling pixels)
def find_nearest_red():
    # Capture a screenshot of the screen
    screen = np.array(ImageGrab.grab())  # Capture full screen as NumPy array
    
    # Get the current mouse position
    mouse_x, mouse_y = pyautogui.position()
    
    min_distance = float('inf')
    nearest_red_pixel = None
    
    # Reduce the search area by sampling every 10th pixel to improve speed
    step = 10  # Increase for faster search but lower accuracy, decrease for more accuracy
    
    for y in range(0, screen.shape[0], step):  # Skip pixels in rows
        for x in range(0, screen.shape[1], step):  # Skip pixels in columns
            pixel = screen[y, x]
            if is_red(pixel):  # If the pixel is red
                distance = np.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_red_pixel = (x, y)
    
    return nearest_red_pixel

# Main function to continuously track the red pixel when 'Alt' is pressed
def main():
    print("Hold 'Alt' to move the mouse to the nearest red pixel. Release to stop.")
    
    while True:
        # If 'Alt' key is held down, move the mouse to the nearest red pixel
        if keyboard.is_pressed('alt'):
            # Find the nearest red pixel
            nearest_red_pixel = find_nearest_red()
            
            if nearest_red_pixel:
                # Move the mouse to the nearest red pixel
                pyautogui.moveTo(nearest_red_pixel)
            
            # Small delay to allow the CPU to breathe, without affecting responsiveness too much
            time.sleep(0.001)  # Reduced delay for faster response
        else:
            # Optional: No action when 'Alt' is not pressed
            time.sleep(0.05)  # Slight delay to reduce CPU usage when not pressing 'Alt'

# Run the main function
if __name__ == "__main__":
    main()
