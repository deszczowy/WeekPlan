from PIL import Image, ImageDraw, ImageColor, ImageFont
from options import WEEKDAYS
from .measurements import Measurements

class Picture:
    # A4 Landscape 300dpi
    WIDTH = 3508
    HEIGHT = 2480

    def __init__(self, file_path, background="white"):
        self.m = Measurements(3508, 2408)
        self.file_path = file_path
        self.font = "./res/noto-sans.regular.ttf"
        self.image = Image.new(
            "RGB",
            (self.m.WIDTH, self.m.HEIGHT),
            background
        )

    def update_measurements_according_to_plan(self, number_of_days, number_of_persons, first_hour, last_hour):
        self.m.update_by_plan(number_of_persons, number_of_days, first_hour, last_hour)
        
    def print_border(self):
        self.rectangle(self.m.MARGIN_LEFT, self.m.MARGIN_TOP, self.m.MARGIN_LEFT + self.m.CLIENTW, self.m.CLIENTH)

    # Prints rectangle
    def rectangle(self, x1, y1, x2, y2, outline=None, width=2, fill=None):
        draw = ImageDraw.Draw(self.image)
        color = None

        if fill is not None:
            color = ImageColor.getrgb(fill)

        draw.rectangle(
            (x1, y1, x2, y2),
            outline=outline,
            width=width,
            fill=color
        )

    # Prints text on given position
    def text(self, x, y, caption, size):
        draw = ImageDraw.Draw(self.image)
        ufont = ImageFont.truetype(self.font, size)
        p = (x, y)
        draw.text(p, caption, fill="black", font=ufont)

    # Measuring text length in pixels
    def text_length(self, text, size) -> int:
        draw = ImageDraw.Draw(self.image)
        ufont = ImageFont.truetype(self.font, size)
        return draw.textlength(text, font=ufont, font_size=size)
        

    # Prints grid on a paper
    def grid(self):
        stepy = self.m.CLIENTH / self.m.HOURS
        draw = ImageDraw.Draw(self.image)

        for i in range(0,self.m.HOURS):
            y = i * stepy
            p1 = (self.m.MARGIN_LEFT, self.m.MARGIN_TOP + y)
            p2 = (self.m.MARGIN_LEFT + self.m.CLIENTW, self.m.MARGIN_TOP + y)
            points = [p1, p2]
            draw.line(points, fill="black", width=1)
            self.text(p1[0], p1[1], "{0}:00".format(self.m.FIRST_HOUR_TIME + i), 25)

        start_line = self.m.MARGIN_LEFT + self.m.GUTTER

        for i in range(0,self.m.DAYS):
            x = i * self.m.DAY_WIDTH
            p1 = (start_line + x, self.m.MARGIN_TOP)
            p2 = (start_line + x, self.m.CLIENTH)
            points = [p1, p2]
            draw.line(points, fill="blue", width=1)

    def print_labels(self):
        draw = ImageDraw.Draw(self.image)
        start_line = self.m.MARGIN_LEFT + self.m.GUTTER

        for i in range(0, self.m.DAYS):
            xd = i * self.m.DAY_WIDTH
            x = start_line + xd
            y = 0
            self.text(x, y, WEEKDAYS[i], 40)

    def save(self):
        self.image.save(self.file_path)