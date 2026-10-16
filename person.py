from datetime import datetime, time

"""
Osoba, której zajęcia są obecne na planie.
Zawiera definicje koloru pozycji na planie, nazwę osoby i wszystkie jej zadania w tygodniu.
"""
class Person:
    def __init__(self, name, color, lines):
        self.order = 0
        self.name = name
        self.color = color
        self.lines = lines

    def get_day(self, symbol):
        vs = []
        for l in self.lines:
            if l.weekday == symbol:
                vs.append(l)
        return vs

    def get_minimum_time(self):
        mt = datetime.strptime("2359", "%H%M").time()

        for l in self.lines:
            if l.start < mt:
                mt = l.start
        return mt

    def get_maximum_time(self):
        mt = datetime.strptime("0000", "%H%M").time()

        for l in self.lines:
            if l.end > mt:
                mt = l.end
        return mt
