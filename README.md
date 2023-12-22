# Automated Mouse and Keyboard Script

This Python script utilizes the `pyautogui` library to automate mouse movements and keyboard actions at regular intervals.

## Installation

1. Install Python: [Python Installation Guide](https://www.python.org/downloads/)
2. Install required library:
   ```bash
   pip install pyautogui


   
import pyautogui
import time

# Disable failsafe to prevent accidental interruption of the script
pyautogui.FAILSAFE = False

# Infinite loop to keep the automation running continuously
while True:
    # Pause for 15 seconds before executing the next set of actions
    time.sleep(15)
    
    # Move the mouse to the coordinates (50, 50)
    for i in range(50, 51):
        pyautogui.moveTo(50, i * 50)
    
    # Press the 'Alt' key three times
    for _ in range(3):
        pyautogui.hotkey('alt')
Explanation:
Importing Modules:

pyautogui is used for automating mouse and keyboard actions.
time is used for introducing delays in the script.
Disabling Failsafe:

The failsafe feature of pyautogui is disabled to prevent accidental interruption.
Infinite Loop:

The script runs in an infinite loop to continuously perform the specified actions.
Delay:

The script pauses for 15 seconds in each iteration before executing the next set of actions.
Mouse Movement:

The mouse is moved to the coordinates (50, 50).
Keyboard Actions:

The 'Alt' key is pressed three times. Modify this part based on specific keyboard actions.
Feel free to customize the script according to your automation needs.
