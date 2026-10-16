class Measurements:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.MARGIN_LEFT = 70
        self.MARGIN_TOP = 50
        self.GUTTER = 80
        self.PADDING = 5
        self.CLIENTW = self.WIDTH - (2 * self.MARGIN_LEFT)
        self.CLIENTH = self.HEIGHT - (2 * self.MARGIN_TOP)

        # Wskazania do aktualizacji w zależności od planu
        self.MINUTE = 1 # wielkość minuty w pixelach
        self.FIRST_HOUR = self.MARGIN_TOP # położenie linii pierwszej godziny
        self.DAY_WIDTH = self.MARGIN_TOP # szerokość kolumny dla dnia
        self.ACTIVITY_WIDTH = self.MARGIN_TOP # szerokość prostokata aktywności w kolumnie dnia
        self.DAYS = 7
        self.FIRST_HOUR_TIME = 8
        self.LAST_HOUR_TIME = 16
        self.PERSONS_COUNT = 1
        self.HOURS = 8
        self.MINUTES_WHOLE_DAY = 0

    def update_by_plan(self, persons, days, first_hour, last_hour):
        self.DAYS = days
        self.FIRST_HOUR_TIME = first_hour
        self.LAST_HOUR_TIME = last_hour
        self.HOURS = last_hour - first_hour + 1
        self.PERSONS_COUNT = persons
        self.MINUTES_WHOLE_DAY = self.HOURS * 60
        self.MINUTE = self.CLIENTH / self.MINUTES_WHOLE_DAY
        self.DAY_WIDTH = (self.CLIENTW - self.GUTTER) / self.DAYS
        self.ACTIVITY_WIDTH = self.DAY_WIDTH / self.PERSONS_COUNT
    
    def print(self):
        print("w {0}, h {1}".format(self.WIDTH, self.HEIGHT))
        print("cw {0}, ch {1}".format(self.CLIENTW, self.CLIENTH))
        print("days {0}".format(self.DAYS))
        print("from {0}h to {1}h = {2}h = {3}min whole day".format(self.FIRST_HOUR_TIME, self.LAST_HOUR_TIME, self.HOURS, self.MINUTES_WHOLE_DAY))

