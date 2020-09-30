from PIL import Image,ImageDraw, ImageChops


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


def encode_image(path_to_png,text_to_write):
    """
     Add docstring and complete implementation.
    """
    #read original image 
    og_image = Image.open(path_to_png)
    #create new image to encode 
    new_image = Image.new('RGB', og_image.size)
    base_red_channel = og_image.getchannel(0)
    green_channel = og_image.getchannel(1)
    blue_channel = og_image.getchannel(2)
    x_size, y_size = og_image.size
    secret_img = write_text(text_to_write, (x_size, y_size))
    for row in og_image:
        for pixel in row:
            red_pixel = base_red_channel.getpixel((row,pixel))
            green_pixel = green_channel.getpixel((row,pixel))
            blue_pixel = blue_channel.getpixel((row,pixel))

            new_image.putpixel((row,pixel), (red_pixel, green_pixel, blue_pixel))
            if red_pixel % 2 == 1:
                # make it even
                red_pixel -= 1
                new_image.putpixel((row,pixel), (red_pixel, green_pixel, blue_pixel))
            
            encoded_image = ImageChops.add(new_image, secret_img)
            encoded_image.save("encoded_sun_image.png")
            

    

def write_text(text_to_write, img_size):
    """
    Add docstring and complete implementation.
    """
       # create an image
    img_enc = Image.new("RGB", img_size, (1,0,0))

    # get a drawing context
    d = ImageDraw.Draw(img_enc)

    # draw multiline text
    d.multiline_text((10,10), text_to_write, fill=(0, 0, 0))

    return img_enc
  

if __name__ == "__main__":
   encode_image("sun_image.png", "hello sunshine")