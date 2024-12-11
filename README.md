# Aid for Aiming booster

A Python-based program that automatically moves the mouse cursor to the nearest red pixel on the screen when holding the 'Alt' key. This mimics the behavior of an aimbot, similar to those used in shooting games, but designed to interact with screen pixels based on color.

## **Description**

This project is designed to help automate the mouse cursor to move towards the nearest red pixel when the user holds down the 'Alt' key. The program continuously tracks the red pixels on the screen and follows them with the mouse cursor. The cursor stops following the red pixels once the 'Alt' key is released.

**Disclaimer**: This program is for educational purposes only. Use responsibly and ensure you are not violating any game's terms of service by using this type of automation.

## Features

- **Mouse Follow**: When holding the 'Alt' key, the mouse cursor follows the nearest red pixel on the screen.
- **Auto-tracking**: Continuously tracks and moves the cursor to the nearest red pixel.
- **Stop Tracking**: Once the 'Alt' key is released, the program stops moving the cursor.
- **Real-Time Feedback**: The program operates in real-time, tracking changes in the display.

## **Technologies Used**

- **Language**: Python
- **Libraries**:
  - `pyautogui`: For controlling the mouse.
  - `keyboard`: For detecting key presses.
  - `Pillow`: For screen capture and pixel analysis.
  - `numpy`: For handling pixel data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mouri69/Aimbot.git
   cd Aimbot
   ```
2. Install dependencies:
   ```bash
   pip install pyautogui keyboard pillow numpy
   ```
3. Run the application:
   ```bash
   python aimbot.py
   ```

## Usage

1. Press and hold the 'Alt' key to make the mouse cursor automatically move to the nearest red pixel on your screen.
2. Release the 'Alt' key to stop the cursor from following the red pixels.
   
You can customize the program to track different colors by modifying the pixel color logic inside the code.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Created by [Mouri69](https://github.com/Mouri69).

