from PIL import Image, ImageDraw, ImageColor, ImageFont
import random
import math

def lumina():
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


class Captions:

    def __init__(self, wrapping_method: str, font: str) -> None:
        self.method = wrapping_method
        self.font = font
    
    def get(self, caption: str, font_size: int, max_width: int) -> [str]:
        ufont = ImageFont.truetype(self.font, font_size)
        if self.method == "w": #wrap
            return self._multiline(ufont, caption, max_width)
        if self.method == "c": #cut
            return self._cut(ufont, caption, max_width)
        if self.method == "s": #short
            return self._short(ufont, caption, max_width)

    def _multiline(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        
        lines = []

        for p in text.splitlines() or [""]:
            words = p.split()
            line = ""

            for w in words:
                txt = f"{line} {w}".strip()

                if font.getlength(txt) <= limit_px:
                    line = txt
                    continue

                if line:
                    lines.append(line)
                    line = ""

                # split the word if exceedes the limit
                part = ""
                for char in w:
                    txt = part + char
                    if part and font.getlength(txt) > limit_px:
                        lines.append(part)
                        part = char
                    else:
                        part = txt

                line = part

            if line or not words:
                lines.append(line)

        return lines
    
    def _cut(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        return ["cut"]

    def _short(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        return ["short"]

    def _get_length(self, text: str, size: int) -> float:
        return ImageFont.truetype(self.font, size).getlength(text)

def captions():
    c = Captions("w", "noto-sans.regular.ttf").get("Testing long activities names", 20, 200)
    print(c)

captions()

