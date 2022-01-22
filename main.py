from numpy import array
import PIL.Image
import PIL.ImageTk
from collections import Counter

from colormap import rgb2hex
from tkinter import *
from tkinter import filedialog
from windows import set_dpi_awareness

# Note: Due to DPI awareness, the font size needs to be reasonably large
THEME_FONT = ("Arial", 22, "normal")
NUM_VALUES = 15


class ImageReader:

    def __init__(self):
        self.window = Tk()
        self.window.title("Image Reader Utility: Create Color Palettes from Images")
        set_dpi_awareness()

        self.canvas = Canvas(width=1000, height=750, bg="#000")
        self.canvas.grid(row=0, column=0)

        self.button = Button(text="Select Image", font=THEME_FONT, command=self.get_color_values)
        self.button.grid(row=1, column=0)

        self.window.mainloop()

    def get_color_values(self):
        img = PIL.Image.open(fp=filedialog.askopenfilename())
        img_array = array(img)
        rgb_values = []

        for row in img_array:
            rgb_values = [value.tolist() for value in row]

        hex_values = [rgb2hex(value[0], value[1], value[2]) for value in rgb_values]
        top_values = Counter(hex_values).most_common(NUM_VALUES)
        self.display_color_values(top_values)

    def display_color_values(self, values):
        # Clear out any existing colors or hex codes
        self.canvas.delete("color")
        self.canvas.delete("hex_code")
        starting_x = 0
        starting_y = 0
        for value in values:
            color = value[0]
            self.saved_colors.append(color)
            self.canvas.create_rectangle(starting_x, starting_y, starting_x + 150, starting_y + 150, fill=color, tags="color")
            self.canvas.create_text(starting_x + 235, starting_y + 75, fill='#fff', font=THEME_FONT, text=color, tags="hex_code")
            starting_y += 150
            if starting_y >= 750:
                starting_x += 333
                starting_y = 0

ImageReader()