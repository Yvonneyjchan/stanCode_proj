"""
File: fire.py
Name: Yvonne Chan
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    This program shows how to detect fires and highlight them.
    Also, to turn others into gray scale.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()

    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: SimpleImage, the original image
    :return: SimpleImage, the updated image with highlight fires.
    """
    highlighted_fire = SimpleImage(filename)
    for pixel in highlighted_fire:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg*HURDLE_FACTOR :
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlighted_fire


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
