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
  -Initializing the 1.14" display https://www.waveshare.com/wiki/1.14inch_LCD_Module
  -Setting up the camera https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708/#standard-imx708-camera-module-3
  -Installing OpenCV lite https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html

## Step 1: Setting Up the Hardware

### 1.1 Wiring the raspberry pi to the camera and display


### 1.2 Flash the SD card with the appropriate image


### 1.3 Setup VNC access 

### 1.4 Setup a static IP for the Raspberry Pi
    skipping this step 

### 1.5 LCD Module Setup

### 1.6 Arducam Module 3 setup
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