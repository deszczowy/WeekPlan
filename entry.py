from datetime import datetime, time


class Entry:
    def __init__(self, weekday, start, end, label):
        self.weekday = weekday
        self.start = self.get_time(start)
        self.end = self.get_time(end)
        self.label = label
        self.mins = self.diff(self.start, self.end)

    def get_time(self, value) -> time:
        return datetime.strptime(value, "%H%M").time()

    def diff(self, start: time, end: time) -> int:
        return (
            end.hour * 60 + end.minute
            - start.hour * 60 - start.minute
        )

    def offset(self, cut_off) -> int:
        return ((self.start.hour - cut_off) * 60) + self.start.minute

    def duration(self) -> int:
        return (
            self.end.hour * 60 + self.end.minute
            - self.start.hour * 60 - self.start.minute
        )