# Interfacing Raspberry Pi Zero 2 W with Arducam Module 3 and 1.14" LCD module

## Introduction

This repo will serve as a step-by-step guide on how to interface a raspberry pi zero 2 w with a Arducam module 3 (IMX708 sensor), a 1.14" LCD display screen (ST7789 Driver), and a board-mounted tactile switch (or any switch for that matter).

## Prerequisites

- **Hardware:**
  - Raspberry Pi Zero 2 w https://a.co/d/5vl7Fxk
  - Arducam module 3 for raspberry pi with ribbon cable https://a.co/d/4OyNcka
  - 1.14" LCD Display module https://a.co/d/4hXdnB6
  - board-mounted tactile switch https://a.co/d/65UapIX
  - MicroSD card (256 is probably overkill) https://a.co/d/5TTvkYf
  - Power supply
  - For troubleshooting: HDMI mini to HDMI cable, micro USB to female USB A,  monitor, bluetooth mouse + keyboard combo
  
- **Software:**
  - Raspberry Pi Imager 
  - Internet connection for software updates (optional but recommended)
  - VNC Viewer

- **Very Helpful Links:**
  - Initializing the 1.14" display https://www.waveshare.com/wiki/1.14inch_LCD_Module
  - Setting up the camera https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708/#standard-imx708-camera-module-3
  - Installing OpenCV lite https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html

## Step 1: Setting Up the Hardware

### 1.1 Wiring the 1.14" display to the Rpi

<img width="1073" alt="Screenshot 2024-09-15 at 1 10 57 PM" src="https://github.com/user-attachments/assets/69d9f257-41db-46fa-828c-79a825819ba0">

Pins 9 and 10 are for the button. 

### 1.2 Connecting the 12MP IMX708 Arducam Module 3 Camera
<img width="694" alt="Screenshot 2024-09-15 at 1 36 40 PM" src="https://github.com/user-attachments/assets/16cc5374-b61a-4a47-bb3c-6a3b0b9aa877">

Note that ribbon cable may be different for RPi zero 2W and other versions. I am using the ribbon cable that came with the camera. The leads face down (blue end) on the pi, the leads face up (silver end) on the camera

### 1.3 Flash the SD card with the image
Start the Raspberry Pi imager (I'm using v1.8.5)

Click **CHOOSE DEVICE** and choose the appropriate device (Raspberry Pi Zero 2 W)

Click **CHOOSE OS** and choose a 32-bit port of Bullseye. I will be using the *Raspberry Pi OS (Legacy, 32-bit)* release.

Click **CHOOSE STORAGE** and choose the appropriate device. Click **NEXT**.

When prompted to customize your settings, click **EDIT SETTINGS** and make any adjustments you would like. I use this opportunity to set up the wireless internet connection. Note: make sure the hostname remains *raspberrypi*

Click **SAVE** followed by **YES**. Click **YES** again to erase and reformat the SD card.

Hit **CONTINUE** at the pop up screen, and move the SD card to the  unpowered raspberry pi.

### 1.4 Setup VNC access 
Connect the RPI to a monitor with a HDMI mini to HDMI cable. Connect the keyboard and mouse.

Connect the RPI to power and let the system boot up.

We then need to enable VNC access and retrieve the IP address of the RPI

1. Bring up the terminal and type:
   
   ```bash
   hostname -I

This will give you the IP address to use in VNC viewer from your computer.

2. Bring up the system configuration screen with:
   
   ```bash
   sudo raspi-config

Navigate down to **Interface Options** and press <kbd>Enter</kbd> to continue. 

Navigate down to **VNC**, press <kbd>Enter</kbd> to proceed, and press <kbd>Enter</kbd> to confirm **YES** to enable the server.

While we are here, lets enable **SPI** as well. 

3. Bring up VNC Viewer and type in the IP address of the RPi. This will allow you to control the RPi without an extra monitor or mouse + keyboard.

4. Remove HDMI cable and mouse + keyboard

### 1.5 Setup a static IP for the Raspberry Pi
A static IP address should be established for the RPi



## Step 2: Configuring the Software

### 2.1 Boot Up and Update

1. Power on the Raspberry Pi.
2. Open the terminal.
3. Update the system:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade

### 2.2 Installing OpenCV lite

Here we will summerize the contents from this page
https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html
describing how to install OpenCV lite

1. Increase the swapping space for the RPi by typing:
   ```bash
   sudo nano /etc/dphys-swapfile
   ```
   Changing the CONF_SWAPSIZE value to 512:
   ```ini
    CONF_SWAPSIZE = 512

Save by pressing <kbd>CTRL</kbd>+<kbd>S</kbd> followed by <kbd>CTRL</kbd>+<kbd>X</kbd> to exit. 

2. Reboot the system
   ```bash
   sudo reboot

Connect to the RPi with VNC viewer after the system has restarted


3. Install third party software (see link above for details). These can be directly copy and pasted to terminal.
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install build-essential cmake git pkg-config
    sudo apt-get install python3-dev python3-numpy
    sudo apt-get install python-dev python-numpy
    sudo apt-get install libjpeg-dev libpng-dev
    sudo apt-get install libavcodec-dev libavformat-dev
    sudo apt-get install libswscale-dev libdc1394-22-dev
    sudo apt-get install libv4l-dev v4l-utils
    sudo apt-get install libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
    sudo apt-get install libtbb2 libtbb-dev

4. Download and install OpenCV by typing:
    ```bash
    cd~git clone --depth=1 https://github.com/opencv/opencv.git
    cd opencv
    mkdir build
    cd build

5. Copy and paste this in terminal:
    ```bash
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D ENABLE_NEON=OFF \
          -D ENABLE_VFPV3=OFF \
          -D BUILD_ZLIB=ON \
          -D BUILD_OPENMP=OFF \
          -D BUILD_TIFF=OFF \
          -D BUILD_OPENJPEG=OFF \
          -D BUILD_JASPER=OFF \
          -D BUILD_OPENEXR=OFF \
          -D BUILD_WEBP=OFF \
          -D BUILD_TBB=OFF \
          -D BUILD_IPP_IW=OFF \
          -D BUILD_ITT=OFF \
          -D WITH_OPENMP=OFF \
          -D WITH_OPENCL=OFF \
          -D WITH_AVFOUNDATION=OFF \
          -D WITH_CAP_IOS=OFF \
          -D WITH_CAROTENE=OFF \
          -D WITH_CPUFEATURES=OFF \
          -D WITH_EIGEN=OFF \
          -D WITH_GSTREAMER=ON \
          -D WITH_GTK=ON \
          -D WITH_IPP=OFF \
          -D WITH_HALIDE=OFF \
          -D WITH_VULKAN=OFF \
          -D WITH_INF_ENGINE=OFF \
          -D WITH_NGRAPH=OFF \
          -D WITH_JASPER=OFF \
          -D WITH_OPENJPEG=OFF \
          -D WITH_WEBP=OFF \
          -D WITH_OPENEXR=OFF \
          -D WITH_TIFF=OFF \
          -D WITH_OPENVX=OFF \
          -D WITH_GDCM=OFF \
          -D WITH_TBB=OFF \
          -D WITH_HPX=OFF \
          -D WITH_EIGEN=OFF \
          -D WITH_V4L=ON \
          -D WITH_LIBV4L=ON \
          -D WITH_VTK=OFF \
          -D WITH_QT=OFF \
          -D BUILD_opencv_python3=ON \
          -D BUILD_opencv_java=OFF \
          -D BUILD_opencv_gapi=OFF \
          -D BUILD_opencv_objc=OFF \
          -D BUILD_opencv_js=OFF \
          -D BUILD_opencv_ts=OFF \
          -D BUILD_opencv_dnn=OFF \
          -D BUILD_opencv_calib3d=OFF \
          -D BUILD_opencv_objdetect=OFF \
          -D BUILD_opencv_stitching=OFF \
          -D BUILD_opencv_ml=OFF \
          -D BUILD_opencv_world=OFF \
          -D BUILD_EXAMPLES=OFF \
          -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
          -D OPENCV_ENABLE_NONFREE=OFF \
          -D OPENCV_GENERATE_PKGCONFIG=ON \
          -D INSTALL_C_EXAMPLES=OFF \
          -D INSTALL_PYTHON_EXAMPLES=OFF ..

5. Start the build:
    ```bash
    make -j$(nproc)

6. Follow with:
    ```bash
    sudo make install
    sudo ldconfig
    sudo apt-get update

7. Remove the OpenCV folder
    ```bash
    cd ~
    sudo rm -rf opencv

8. Check your version of open cv
    ```bash
    python3
    ```
    ```bash
    import cv2
    cv2.__version__

### 2.3 Setting up the LCD module
1. Install libraries (lgpio)
    ```bash
    wget https://github.com/joan2937/lg/archive/master.zip
    unzip master.zip
    cd lg-master
    sudo make install 
    ```
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install spidev 
    ```

2. FBCP Porting, Download the drivers
    ```bash
    sudo apt-get install cmake -y
    cd ~
    wget https://files.waveshare.com/upload/1/18/Waveshare_fbcp.zip
    unzip Waveshare_fbcp.zip
    cd Waveshare_fbcp/
    sudo chmod +x ./shell/*

3. start up the terminal
    ```bash
    sudo nano /boot/config.txt
    ```
    modify hdmi_cvt value 
    ```ini
    hdmi_cvt 640 480 60 1 0 0 0
    ```
Save by pressing <kbd>CTRL</kbd>+<kbd>S</kbd> followed by <kbd>CTRL</kbd>+<kbd>X</kbd> to exit. We change these values temporarily.

4. Run the shell script
    ```bash
    sudo ./shell/waveshare-1inch14

### 2.4 Setting up the camera module
1. Run the shell script
    ```bash
    sudo nano /boot/config.txt 
    ```
    Update the following parameters (ord add if not found):
    ```ini
    camera_auto_detect=0
    dtoverlay=imx708
    ```
    Save and exit
2. Reboot the system.
   ```bash
   sudo reboot

### 2.4 Load and test the script

1. Start by creating a new folder for scripts
   ```bash
   mkdir /home/pi/scripts
   ```
   note your username(mine is pi) may be different

2. create and open a new file
   ```bash
   touch /home/pi/scripts/ArduCam-Snapshot.py
   sudo nano /home/pi/scripts/ArduCam-Snapshot.py
   ```
3. Copy and paste the following script into the file. Save and exit
   ```bash
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
   ```
4. Test the script
   ```bash
   python3 /home/pi/scripts/ArduCam-Snapshot.py
   ```
### 2.5 Starting the script on boot

1. Open terminal and create a systemd service to start the script on boot:
  
   ```bash
   sudo touch /etc/systemd/system/ArduCam-Snapshot.service

2. Open the service file:
   
   ```bash
   sudo nano /etc/systemd/system/ArduCam-Snapshot.service

3. Initialize the service file with the appropriate values:

   ```ini
    [Unit]
    Description= Service to start the camera on boot
    After=multi-user.target

    [Service]
    ExecStart=/usr/bin/python3 /home/pi/scripts/ArduCam-Snapshot.py
    StandardOutput=inherit
    StandardError=inherit
    Restart=always
    User=pi  ##change this value accordingly
    Environment=DISPLAY=:0

    [Install]
    WantedBy=multi-user.target

4. Save by pressing <kbd>CTRL</kbd>+<kbd>S</kbd> followed by <kbd>CTRL</kbd>+<kbd>S</kbd> to exit

5. Reload systemmd and restart the service:
   
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart Arducam_Snapshot.service
6. After restarting, check if the service is running correctly:

    ```bash
    sudo systemctl status feed.service

7. Perform a system reboot. The service should start the script on its own!

    ```bash
    sudo reboot

8. You may want to stop the service. Exit the script by pressing  <kbd>Q</kbd>. Navigate to the terminal and type

    ```bash
    sudo systemctl stop ArduCam-Snapshot.service

9. Disable the service so that it does not restart again


    ```bash
    sudo systemctl disable ArduCam-Snapshot.service

This should disable the service from restarting, allowing you to continue troubleshooting the project
