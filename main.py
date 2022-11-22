from turtle import *
from PIL import Image;

img = Image.open('image.jpg').convert('RGB')

colormode(255)
setworldcoordinates(-1, img.height, img.width, -1)
pendown()
speed(500)

for y in range(img.height):
    for x in range(img.width):
        pendown()
        goto(x, y)
        color(img.getpixel((x, y)))
        forward(1)
    penup()
    goto(0, x)

done()
