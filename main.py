from subprocess import list2cmdline
from PIL import Image
#from functions.cipher import vigenere_cipher,cesar_cipher
picture=Image.open("images/shop.png").convert("RGB")


def get_img_pixel(x,y,image):
    
    pixels=image.getpixel((x,y))
    if pixels != "none":
        print(pixels)
    else:
        print("No conversion")
    return pixels
get_img_pixel(12,40,picture)
 
def binary_text(text):
    ascii_text_list=[ord(letter) for letter in text]
    
    binary_list_text= "".join(list(map(lambda asciilistvalue: bin(asciilistvalue),ascii_text_list)))
    
    print(f"the Text :'{text.upper()}' -> conversion in binary is {binary_list_text}")  
    
    return binary_list_text

binary_text("je mange du riz")
    
