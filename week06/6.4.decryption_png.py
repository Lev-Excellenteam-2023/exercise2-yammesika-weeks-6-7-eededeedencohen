#-------------------
# זכרו זכרו - 6.4
#-------------------
from check_type_decorator import check_type

#============================================
# streps: 
# 1.  get the image from the path.
# 2.  for each column in the image: 
# 2.1 find the black pixel and get the number on the row.
# 2.2 convert the number to a char.
# 2.3 add the char to the message.
#============================================

from PIL import Image


# all of this to function:
@check_type(str)
def decode_image(image_path):
    # get the image
    im = Image.open(image_path)

    # get the image width with Image
    width = im.size[0]

    # get the image height with Image
    height = im.size[1]

    # create a list of lists of the pixels in the image. each list in the list is a column.
    all_columns = [[im.getpixel((i,j)) for j in range(height)] for i in range(width)]

    # decode the message by finding the index of the black pixel in each column.
    return "".join([chr(column.index(1)) for column in all_columns])

# main function
def main():
    # get the image path
    image_path = "resources/code.png"

    # decode the image
    message = decode_image(image_path)

    # print the message
    print(message)

# run the main function
if __name__ == "__main__":
    main()













