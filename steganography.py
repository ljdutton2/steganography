from PIL import Image


def decode_image(path_to_png):
    
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    #pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            # convert each red channel pixel value to binary string
            binary = bin(red_channel.getpixel((x,y)))
            # check if string ends in 0 or 1
            count = len(binary)
            lsb = binary[count-1]
            # ends in 0, pixel at x_size, y_size = black
            if lsb == "0":
                decoded_image.putpixel((x,y), (0,0,0))
            # ends in 1, pixels at x_size, y_size = white
            else:
                decoded_image.putpixel((x,y), (255,255,255))
    
    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

if __name__ == "__main__":
    decode_image('encoded_image.png')