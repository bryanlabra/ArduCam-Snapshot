# Interfacing Raspberry Pi zero 2 w with Arducam Module 3 and 1.14" LCD module

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

## Step 1: Setting Up the Hardware

### 1.1 Flash the sd card

Ensure the Raspberry Pi is shut down and unplugged before connecting the camera.

### 1.2 Connect the Camera Module

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