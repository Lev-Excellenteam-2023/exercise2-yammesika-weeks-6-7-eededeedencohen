#----------------
# זכרתם? - 6.5
#----------------
from check_type_decorator import check_type


#====================================================
# encryption_png function:
# get a message.
# return encryption of the message in png format.
#====================================================
from PIL import Image


@check_type(str)
def encryption_png(message):
    askii_numbers = [ord(char) for char in message]

    """ Image.new: 
     L - 8-bit pixels, black and white.
     2nd argument - size of the image - (width, height)
     3rd argument - color of the background - 255 is white
    """
    im = Image.new("L", (len(askii_numbers), 256), 255)
    for column in range(len(askii_numbers)):
        im.putpixel((column, askii_numbers[column]), 1)
    im.save("resources/decode.png")

# main function
def main():
    # get the message
    message = "Eden is the best!!!!!!!!!!!!!!!"

    # encode the message
    encryption_png(message)

# run the main function
if __name__ == "__main__":
    main()