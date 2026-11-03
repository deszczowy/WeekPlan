from PIL import Image, ImageDraw, ImageColor, ImageFont
import random
import math

w = 400
h = 400
black = ImageColor.getrgb("#000000")
white = ImageColor.getrgb("#FFFFFF")

ufont = ImageFont.truetype("noto-sans.regular.ttf", 40)
image = Image.new("RGB", (w, h), "white")
draw = ImageDraw.Draw(image)

# losowanie back
r = random.randint(1, 255)
g = random.randint(1, 255)
b = random.randint(1, 255)
back = (r,g,b)
front = black

baseline = 128
color = r * g * b

# https://emby.media/learn/articles/video/color-standards/standards/Color-Standard-BT601.html
lumination = (299 * r + 587 * g + 114 * b) / 1000
# 299 + 587 + 114 = 1000

if lumination < baseline:
    front = white

draw.rectangle((0, 0, w, h), fill=back)
draw.text((100, 100), "{0}".format(back), fill=front, font=ufont)
image.save("test.png")