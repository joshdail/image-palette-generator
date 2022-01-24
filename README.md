# image-palette-generator
## Version 2.1.0
Tkinter utility to generate color palettes from jpg and png files

## Required packages: Tkinter, Pillow, Numpy

This app allows you to generate a color palette based on commonly occurring colors in a selected jpg or png file. (PDF files are not supported.)

When you select an image, a palette of 16 colors will be generated from the image. Thumbnails of the colors along with their corresponding hex codes are displayed in the app window.

The previous version of the app simply displayed the most commonly detected hex codes. This could create issues where a certain color was over-represented because the same color with very slight variations in RGB values might appear many times. (For example, a picture with a lot of red might have 15 shades of red that are almost all the same, but because they were the codes with the highest count, the only color that appeared would be red.) This version attempts to use a median cut algorithm to produce a palette that is more representative of the overall picture.

## Latest update:
- Fixed a bug that was causing the program to only extract colors from a subset of the image

## Future:
- Ability to copy the hex code to the clipboard by clicking on the thumbnail
