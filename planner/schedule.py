from datetime import datetime, time
from .entry import Entry
from .person import Person


class Schedule:

    def __init__(self) -> None:
        self.clear()
        # Weekdays symbol
        self.week = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    
    def clear(self) -> None:
        # Week plan description header
        self.header = ""
        # Activities storage. Dictionary where person is the key
        self.data = {}
    
    def add_person(self, label, color, activities) -> None:
        self.data[label] = Person(
            name=label,
            color=color,
            activities=activities
        )

    def get_start_time(self):
        st = datetime.strptime("2359", "%H%M").time()
        for p in self.data:
            day_start = self.data[p].get_minimum_time()
            if day_start < st:
                st = day_start
        return st

    def get_finish_time(self):
        ft = datetime.strptime("0000", "%H%M").time()
        for p in self.data:
            day_end = self.data[p].get_maximum_time()
            if day_end > ft:
                ft = day_end
        return ft

    def show(self) -> None:
        for p in self.data:
            print("===")
            print(self.data[p].name)
            print(self.data[p].color)
            for w in self.week:
                ex = self.data[p].get_day(w)

                for l in ex:
                    print("--")
                    print(l.weekday)
                    print(l.start)
                    print(l.end)
                    print(l.label)
                    print(l.mins)

            print("-=-")
            print(self.get_start_time())
            print(self.get_finish_time())

    def create_entry(self, weekday, activity_start_time, activity_end_time, activity_label) -> Entry:
        return Entry(
            weekday=weekday,
            start=activity_start_time,
            end=activity_end_time,
            label=activity_label
        )