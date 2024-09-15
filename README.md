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
  - For troubleshooting: HDMI mini to HDMI cable, micro USB to female USB A,  monitor, bluetooth mouse and keyboard combo
  
- **Software:**
  - Raspberry Pi Imager 
  - Internet connection for software updates (optional but recommended)
  - VNC Viewer

- **Very Helpful Links:**
  - Initializing the 1.14" display https://www.waveshare.com/wiki/1.14inch_LCD_Module
  - Setting up the camera https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708/#standard-imx708-camera-module-3
  - Installing OpenCV lite https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html

## Step 1: Setting Up the Hardware

### 1.1 Wiring the 1.14" display to the rpi

<img width="1073" alt="Screenshot 2024-09-15 at 1 10 57 PM" src="https://github.com/user-attachments/assets/69d9f257-41db-46fa-828c-79a825819ba0">

Pins 9 and 10 are for the button. 

### 1.2 Connecting the 12MP IMX708 Arducam Module 3 Camera
<img width="694" alt="Screenshot 2024-09-15 at 1 36 40 PM" src="https://github.com/user-attachments/assets/16cc5374-b61a-4a47-bb3c-6a3b0b9aa877">

Note that ribbon cable may be different for RPI zero 2W and other versions. I am using the ribbon cable that came with the camera. The leads face down (blue end) on the pi, the leads face up (silver end) on the camera

### 1.3 Flash the SD card with the image
Start the Raspberry Pi imager (I'm using v1.8.5)
Click **CHOOSE DEVICE** and choose the appropriate device (Raspberry Pi Zero 2 W)
Click **CHOOSE OS** and choose a port of Bullseye, either 32-bit or 64-bit should work. I will be using the *Raspberry Pi OS (Legacy, 64-bit)* Bullseye release. You may need to click on **Raspberry Pi OS (other)** to find this version.

### 1.4 Setup VNC access 

### 1.5 Setup a static IP for the Raspberry Pi
skipping this step 

### 1.6 LCD Module Setup

### 1.7 Arducam Module 3 Camera setup
- **For the Raspberry Pi Camera Module:**
  1. Locate the CSI (Camera Serial Interface) slot.
  2. Gently lift the plastic clip.
  3. Insert the camera ribbon cable with the metal contacts facing away from the Ethernet port.
  4. Press down the clip to secure the cable.

## Step 2: Configuring the Software

### 2.1 Boot Up and Update

1. Power on the Raspberry Pi.
2. Open the terminal.
3. Update the system:

   ```bash
   sudo apt update && sudo apt upgrade -y

### X.1 Starting the script on boot

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

4. Save by pressing CTRL+S followed by CTRL+X to exit

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

8. You may want to stop the service. Exit the script by pressing q. Navigate to the terminal and type

    ```bash
    sudo systemctl stop ArduCam-Snapshot.service

9. Disable the service so that it does not restart again


    ```bash
    sudo systemctl disable ArduCam-Snapshot.service

This should disable the service from restarting, allowing you to continue troubleshooting the project
