from datetime import datetime, time


class Person:
    def __init__(self, name, color, activities):
        self.order = 0
        self.name = name
        self.color = color
        self.activities = activities

    def get_day(self, symbol):
        vs = []
        for l in self.activities:
            if l.weekday == symbol:
                vs.append(l)
        return vs

    def get_minimum_time(self):
        mt = datetime.strptime("2359", "%H%M").time()

        for l in self.activities:
            if l.start < mt:
                mt = l.start
        return mt

    def get_maximum_time(self):
        mt = datetime.strptime("0000", "%H%M").time()

        for l in self.activities:
            if l.end > mt:
                mt = l.end
        return mt
