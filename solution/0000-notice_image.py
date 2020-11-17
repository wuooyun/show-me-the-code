#!/usr/bin/env python3
from PIL import Image,ImageDraw,ImageFont

imgpath = r"C:\Users\Yun\Pictures\KzVJHOur.gif"
fontpath = r"C:\Windows.old\Windows\Fonts\mmrtext.ttf"

#im = Image.new("RGB",(200,200),"white")

im = Image.open(imgpath).convert("RGBA")
font = ImageFont.truetype(fontpath,48)
d = ImageDraw.Draw(im)
x,y = im.size

d.text((x,0),"4",anchor="rt",fill="red",font=font)
im.show()
