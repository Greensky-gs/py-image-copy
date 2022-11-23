from turtle import *
from PIL import Image;

img = Image.open('image.jpg').convert('RGB')


all_pixels = []

for y in range(img.height):
    for x in range(img.width):
        all_pixels.append(img.getpixel((x, y)));

print("loading finished")
colormode(255)
setworldcoordinates(-1, img.height, img.width, -1)
pendown()

for y in range(img.height):
    for x in range(img.width):
        goto(x, y)
        color(all_pixels[x + y])
        forward(1)
    penup()
    goto(0, x)
    pendown()

done()
