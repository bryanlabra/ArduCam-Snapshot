import cv2
from picamera2 import Picamera2
import time
import os
from datetime import datetime
import RPi.GPIO as GPIO

# Initialize GPIO for button input
GPIO.setmode(GPIO.BCM)
button_pin = 15  # GPIO 15 corresponds to pin 10 on the board
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor

# Initialize PiCamera2
picam2 = Picamera2()

# Set the desired resolution and frame rate (lower for smoother feed)
resolution = (320, 240)  # Lower resolution for smoother performance
frame_rate = 30  # Moderate frame rate for smoother feed

# Configure the camera with the resolution
camera_config = picam2.create_still_configuration(main={"size": resolution})
picam2.configure(camera_config)

# Start the camera
picam2.start()

# Open a named window with OpenCV and set it to fullscreen
cv2.namedWindow("Camera Feed", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera Feed", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Prepare directory for saving images
save_directory = '/home/pi/Pictures/'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Initialize variables for tracking image index and date
current_date = datetime.now().strftime("%y%m%d")
image_index = 1

def capture_photo():
    global image_index, current_date

    # Get the current date
    now = datetime.now()
    new_date = now.strftime("%y%m%d")

    # Reset the index if the date has changed
    if new_date != current_date:
        current_date = new_date
        image_index = 1

    # Create filename based on date and index
    filename = f"{current_date}_{image_index}.jpg"
    image_index += 1

    # Capture the image and save it
    filepath = os.path.join(save_directory, filename)
    picam2.capture_file(filepath)
    
    # Display the image for 2 seconds
    img = cv2.imread(filepath)
    cv2.imshow('Camera Feed', img)
    cv2.waitKey(2000)  # Display for 2 seconds

try:
    while True:
        # Capture frame-by-frame for the live feed
        frame = picam2.capture_array()

        # Convert the frame from BGR to RGB to fix the blue hue issue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the live feed without resizing
        cv2.imshow('Camera Feed', frame)

        # Check if the button is pressed (GPIO 15, LOW when pressed)
        if GPIO.input(button_pin) == GPIO.LOW:
            capture_photo()
            time.sleep(0.2)  # Debounce button to prevent multiple captures

        # Set frame rate delay (in milliseconds)
        if cv2.waitKey(int(1000 / frame_rate)) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
finally:
    # Cleanup GPIO and stop camera
    GPIO.cleanup()
    picam2.stop()
    cv2.destroyAllWindows()
