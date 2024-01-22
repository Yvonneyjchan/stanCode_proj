"""
File: blur.py
Name: Yvonne Chan
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the updated image with blur.
    """
    # Todo: create a new blank img that is as big as the original one

    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            new_p = new_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                tlc_1 = img.get_pixel(x, y+1)
                tlc_2 = img.get_pixel(x+1, y+1)
                tlc_3 = img.get_pixel(x+1, y)
                new_p.red = (pixel.red + tlc_1.red + tlc_2.red + tlc_3.red) // 4
                new_p.green = (pixel.green + tlc_1.green + tlc_2.green + tlc_3.green) // 4
                new_p.blue = (pixel.blue + tlc_1.blue + tlc_2.blue + tlc_3.blue) // 4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                trc_1 = img.get_pixel(x-1, y)
                trc_2 = img.get_pixel(x-1, y+1)
                trc_3 = img.get_pixel(x, y+1)
                new_p.red = (pixel.red + trc_1.red + trc_2.red + trc_3.red) // 4
                new_p.green = (pixel.green + trc_1.green + trc_2.green + trc_3.green) // 4
                new_p.blue = (pixel.blue + trc_1.blue + trc_2.blue + trc_3.blue) // 4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                blc_1 = img.get_pixel(x, y-1)
                blc_2 = img.get_pixel(x+1, y-1)
                blc_3 = img.get_pixel(x+1, y)
                new_p.red = (pixel.red + blc_1.red + blc_2.red + blc_3.red) // 4
                new_p.green = (pixel.green + blc_1.green + blc_2.green + blc_3.green) // 4
                new_p.blue = (pixel.blue + blc_1.blue + blc_2.blue + blc_3.blue) // 4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                brc_1 = img.get_pixel(x-1, y)
                brc_2 = img.get_pixel(x-1, y-1)
                brc_3 = img.get_pixel(x, y-1)
                new_p.red = (pixel.red + brc_1.red + brc_2.red + brc_3.red) // 4
                new_p.green = (pixel.green + brc_1.green + brc_2.green + brc_3.green) // 4
                new_p.blue = (pixel.blue + brc_1.blue + brc_2.blue + brc_3.blue) // 4

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                te_1 = img.get_pixel(x-1, y)
                te_2 = img.get_pixel(x-1, y+1)
                te_3 = img.get_pixel(x, y+1)
                te_4 = img.get_pixel(x+1, y+1)
                te_5 = img.get_pixel(x+1, y)
                new_p.red = (pixel.red + te_1.red + te_2.red + te_3.red + te_4.red + te_5.red) // 6
                new_p.green = (pixel.green + te_1.green + te_2.green + te_3.green + te_4.green + te_5.green) // 6
                new_p.blue = (pixel.blue + te_1.blue + te_2.blue + te_3.blue + te_4.blue + te_5.blue) // 6

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                be_1 = img.get_pixel(x-1, y)
                be_2 = img.get_pixel(x-1, y-1)
                be_3 = img.get_pixel(x, y-1)
                be_4 = img.get_pixel(x+1, y-1)
                be_5 = img.get_pixel(x+1, y)
                new_p.red = (pixel.red + be_1.red + be_2.red + be_3.red + be_4.red + be_5.red) // 6
                new_p.green = (pixel.green + be_1.green + be_2.green + be_3.green + be_4.green + be_5.green) // 6
                new_p.blue = (pixel.blue + be_1.blue + be_2.blue + be_3.blue + be_4.blue + be_5.blue) // 6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                le_1 = img.get_pixel(x, y-1)
                le_2 = img.get_pixel(x+1, y-1)
                le_3 = img.get_pixel(x+1, y)
                le_4 = img.get_pixel(x+1, y+1)
                le_5 = img.get_pixel(x, y+1)
                new_p.red = (pixel.red + le_1.red + le_2.red + le_3.red + le_4.red + le_5.red) // 6
                new_p.green = (pixel.green + le_1.green + le_2.green + le_3.green + le_4.green + le_5.green) // 6
                new_p.blue = (pixel.blue + le_1.blue + le_2.blue + le_3.blue + le_4.blue + le_5.blue) // 6

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                re_1 = img.get_pixel(x, y-1)
                re_2 = img.get_pixel(x-1, y-1)
                re_3 = img.get_pixel(x-1, y)
                re_4 = img.get_pixel(x-1, y+1)
                re_5 = img.get_pixel(x, y+1)
                new_p.red = (pixel.red + re_1.red + re_2.red + re_3.red + re_4.red + re_5.red) // 6
                new_p.green = (pixel.green + re_1.green + re_2.green + re_3.green + re_4.green + re_5.green) // 6
                new_p.blue = (pixel.blue + re_1.blue + re_2.blue + re_3.blue + re_4.blue + re_5.blue) // 6

            else:
                # Inner pixels.
                in_1 = img.get_pixel(x-1, y-1)
                in_2 = img.get_pixel(x, y-1)
                in_3 = img.get_pixel(x+1, y+1)
                in_4 = img.get_pixel(x-1, y)
                in_5 = img.get_pixel(x+1, y)
                in_6 = img.get_pixel(x-1, y+1)
                in_7 = img.get_pixel(x, y+1)
                in_8 = img.get_pixel(x+1, y+1)
                new_p.red = (pixel.red + in_1.red + in_2.red + in_3.red + in_4.red + in_5.red + in_6.red
                             + in_7.red + in_8.red) // 9
                new_p.green = (pixel.green + in_1.green + in_2.green + in_3.green + in_4.green + in_5.green
                               + in_6.green +in_7.green + in_8.green) // 9
                new_p.blue = (pixel.blue + in_1.blue + in_2.blue + in_3.blue + in_4.blue + in_5.blue
                              + in_6.blue + in_7.blue + in_8.blue) // 9

    return new_img


def main():
    """
    This program shows the blur image among the original img.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
