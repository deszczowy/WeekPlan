from options import WeekDaysRange, WEEKDAYS
from planner import Schedule

class DaysSelector:

    def __init__(self, days_range: WeekDaysRange, schedule: Schedule) -> None:
        self.week_days = []
        self.days_range = days_range
        self.schedule = schedule
    
    def get(self) -> []:
        if self.days_range == WeekDaysRange.ALL:
            self._select_all()
        if self.days_range == WeekDaysRange.WEEKEND:
            self._select_weekend()
        if self.days_range == WeekDaysRange.WORKDAYS:
            self._select_workdays()
        if self.days_range == WeekDaysRange.ACTIVE:
            self._select_acive()
        if self.days_range == WeekDaysRange.SCOPE:
            self._select_scope()
        return self.week_days

    def _select_all(self) -> None:
        for day in WEEKDAYS.keys():
            self.week_days.append(day)
    
    def _select_weekend(self) -> None:
        d = list(WEEKDAYS.keys())
        self.week_days = d[5:]
    
    def _select_workdays(self) -> None:
        d = list(WEEKDAYS.keys())
        self.week_days = d[:5]
    
    def _select_acive(self) -> None:
        self.week_days = self._occurences()

    def _select_scope(self) -> None:
        occurences = self._occurences()
        length = len(occurences)
        if length > 1:
            first = occurences[0]
            last = occurences[length -1]
            add = False

            for day in WEEKDAYS.keys():
                if day == first:
                    add = True
                
                if add:
                    self.week_days.append(day)

                if day == last:
                    add = False
        else:
            self.week_days = occurences

    def _occurences(self) -> []:
        d = {}
        o = []
        for day in WEEKDAYS.keys():
            d[day] = 0

        for key in self.schedule.data.keys():
            for entry in self.schedule.data[key].activities:
                d[entry.weekday] += 1

        for key in d.keys():
            if d[key] > 0:
                o.append(key)

        return o