from PIL import Image

picture=Image.open("shop.png").convert("RGB")


def get_img_pixel(x,y,image):
    
    pixels=image.getpixel((x,y))
    if pixels != "none":
        print(pixels)
    else:
        print("No conversion")
    return pixels
get_img_pixel(12,40,picture)

