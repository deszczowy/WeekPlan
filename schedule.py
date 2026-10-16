from datetime import datetime, time


class Schedule:

    def __init__(self):
        # Week plan description header
        self.header = ""
        # Activities storage. Dictionary where 
        self.data = {}
        # Weekdays symbol
        self.week = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

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

    def show(self):
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
