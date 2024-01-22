"""
File: mirror_lake.py
Name: Yvonne Chan
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    This program makes a mirrored image of mt-rainer.jpg.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = SimpleImage.blank(original_mt.width, original_mt.height*2)
    reflected.show()

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_mt_r = original_mt.get_pixel(x, y)

            blank_r = reflected.get_pixel(x, y)
            blank_r.red = original_mt_r.red
            blank_r.green = original_mt_r.green
            blank_r.blue = original_mt_r.blue

            blank_r_2 = reflected.get_pixel(x, reflected.height-1-y)
            blank_r_2.red = original_mt_r.red
            blank_r_2.green = original_mt_r.green
            blank_r_2.blue = original_mt_r.blue
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
