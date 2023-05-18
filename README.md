# Steganography

## Introduction
This Python code implements a simple GUI application using the tkinter and ttkbootstrap modules for steganography. It provides users with the ability to encode and decode hidden messages in an image.

## Requirements
This code was written using Python 3.9. It requires the following Python modules to be installed:

- numpy
- Pillow (PIL)
- ttkbootstrap
- tkinter

To install these modules, use the following command in the terminal:
- pip install numpy Pillow ttkbootstrap

## Usage
To run the application, simply run the steganographie.py file. This will open a GUI window where you can select an image, enter a message to encode or decode, and perform the respective action using the "Encode" or "Decode" button.

## Menu
File:
- Open: This allows you to open an image file in .jpg or .png format.
- Save: This allows you to save the image with the encoded message as a .png or .jpg file.
- Exit: This allows you to exit the application.

Help:
- About: This displays information about the application.

## GUI Elements
**Message Entry:** This is where you can enter the message to be encoded or decode.

**Canvas:** This displays the image file selected.

**Buttons:**

- Encode: This encodes the entered message in the selected image file.
- Decode: This decodes the message hidden in the selected image file.

# Disclaimer
**This application was made for educational purposes only. The author does not condone or promote the use of steganography for illegal or unethical purposes.**
