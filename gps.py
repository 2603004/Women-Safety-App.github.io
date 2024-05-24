import keyboard
import subprocess
import threading

# Global variable to keep track of space bar presses
space_bar_count = 0

# Define the function to be called when a key is pressed
def on_key_press(event):         
    global space_bar_count
    
    # Check if the pressed key is the space bar
    if event.name == 'space':
        space_bar_count += 1
        
        # If space bar is pressed three times, open the application
        if space_bar_count == 3:
            open_application()

# Function to open the application
def open_application():
    try:
        # Replace 'notepad.exe' with the path or name of the application you want to open
        subprocess.Popen(['notepad.exe'])
    except Exception as e:
        print("Error:", e)

# Start listening for key presses
keyboard.on_press(on_key_press)

# Start the application in a separate thread
app_thread = threading.Thread(target=open_application)
app_thread.start()

# Keep the program running
keyboard.wait('esc')                     
                    