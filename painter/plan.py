from datetime import datetime
from planner import Schedule
from options import Options, SortOrder, TitlePosition, WEEKDAYS
from .picture import Picture


class Plan(Picture):

    def __init__(self, options: Options, schedule: Schedule, logger: Logger, background="white"):
        super().__init__(options.output_file_name, background)
        self.logger = logger
        self.options = options
        # We need full schedule to print the plan sheet
        self.schedule = schedule
        # We need to prepare printout based on the schedule
        self.initial_setups()
        # Build the whole thing
        self.print_border()
        self.grid()
        self.print_labels()
        self.print_schedule_title()
        self.build()
        # Save to file
        self.save()
        # Done.

    def initial_setups(self):
        self.set_time_offsets()
        self.set_number_of_persons()
        self.sort_persons()
        self.update_measurements_according_to_plan(6, self.persons_no, self.first_hour, self.last_hour)
        self.build_days_offset_dictionary()
        self.logger.debug(self.m.print())

    def set_time_offsets(self):
        """
        This is the time baseline of entire plan. It is represented 
        by amount of minutes from midnight when baseline activity starts. 
        This time_offset value will be substract from every activity start time
        to get number of minutes from baseline.
        """
        start = self.schedule.get_start_time()
        end = self.schedule.get_finish_time()

        self.time_offset = (start.hour * 60) + start.minute
        self.first_hour = start.hour
        self.last_hour = end.hour
    
    def set_number_of_persons(self):
        self.persons_no = len(self.schedule.data)
    
    def sort_persons(self) -> None:
        self.persons = list(self.schedule.data.keys())
        if self.options.sort_order == SortOrder.A_TO_Z:
            self.persons.sort(reverse=False)
        if self.options.sort_order == SortOrder.Z_TO_A:
            self.persons.sort(reverse=True)

    def build_days_offset_dictionary(self):
        self.days_offsets = {}
        off = 0
        for day in WEEKDAYS:
            self.days_offsets[day] = off * self.m.DAY_WIDTH
            off +=1

    def build(self):
        po = 0
        for key in self.persons:
            po += 1
            person = self.schedule.data[key]
            person.order = po
            for e in person.activities:
                self._print_activity(person, e)
            self.print_person_description(person)
    
    def print_schedule_title(self) -> None:

        self.title_offset = 0

        if self.options.title_position is not TitlePosition.HIDDEN:
            txt = self.schedule.header
            fsize = 25
            title_length = self.text_length(txt, fsize)
                
            x = 0
            y = self.m.CLIENTH + self.m.PADDING    

            if self.options.title_position == TitlePosition.LEFT:
                x = self.m.MARGIN_LEFT + self.m.GUTTER    
                self.title_offset = title_length + self.m.GUTTER
            else: # TitlePosition.RIGHT
                x = self.m.MARGIN_LEFT + self.m.CLIENTW - title_length          
            
            self.text(x, y, txt, fsize)
    
    def print_person_description(self, person):
        x = self.m.MARGIN_LEFT + self.m.GUTTER + self.title_offset
        y = self.m.CLIENTH + self.m.PADDING
        m = 300 # self.m.CLIENTW / self.m.PERSONS_COUNT
        w = 50
        x += (person.order -1) * m

        self.rectangle(x, y, x + w, y + 30, fill=person.color)
        self.text(x + w + 10, y, person.name, 25)

    def _print_activity(self, person, entry):
        activity_width = self.m.DAY_WIDTH / self.m.PERSONS_COUNT

        x1 = self.m.MARGIN_LEFT + self.m.GUTTER + self.m.PADDING + self.days_offsets[entry.weekday]  + (activity_width * (person.order-1))
        y1 = self.m.MARGIN_TOP + (entry.offset(self.m.FIRST_HOUR_TIME) * self.m.MINUTE)

        x2 = x1  + activity_width - (2 * self.m.PADDING)
        y2 = y1 + (entry.duration() * self.m.MINUTE)

        self.rectangle(x1, y1, x2, y2, fill=person.color)

        x1 += self.m.PADDING
        y1 += self.m.PADDING
        self.text(x1, y1, entry.label, 30)

        y1 += self.m.PADDING + 35
        t1 = entry.start.strftime("%H:%M")
        t2 = entry.end.strftime("%H:%M")
        label = "{0} - {1}".format(t1, t2)
        self.text(x1, y1, label, 20)
        pass