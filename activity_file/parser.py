from planner import Schedule
from options import Options, WEEKDAYS
from .reader import Reader
from .validator import Validator


class Parser:

    def __init__(self, options: Options, schedule: Schedule, logger) -> None:
        self.schedule = schedule
        self.schedule.clear()
        self.options = options
        self.file = self.options.input_file_name
        self.logger = logger
        self.lines = []
        self.index = 0 

    def parse(self) -> None:
        if self.data_is_present():
            if self.data_is_valid():
                self.index = 0
                self.set_header()
                self.set_context()
                self.set_data()
                self.logger.notice("Data gathered.")
                return True
        
        self.logger.notice("Stop.")
        return False

    def data_is_present(self) -> bool:
        return Reader(
            self.file,
            self.logger
        ).get(self.lines)

    def data_is_valid(self) -> bool:
        errors = Validator().validate(self.lines)
        if len(errors) > 0:
            self.logger.notice("Incorrect input file")
            for rule in errors:
                self.logger.notice(rule.to_string())
            return False
        return True
   
    def set_header(self) -> None:
        self.schedule.header = self.lines[self.index]
        self.logger.notice("Reading \"{0}\".".format(self.schedule.header))
        self.index += 1
    
    def set_context(self) -> None:
        is_context_present = False

        if self.lines[self.index].startswith("{"):
            is_context_present = True
            self.index += 1

            while is_context_present:
                day, alias = self.lines[self.index].split("|", 1)
                WEEKDAYS[day] = alias

                self.index +=1
                if self.lines[self.index].startswith("}"):
                    is_context_present = False
                    self.index +=1



    def set_data(self) -> None:
        current_label = None
        current_color = None
        current_lines = []

        for line in self.lines[self.index:]:
            if line.startswith("["):
                color, label = line[1:].split("|", 1)

                current_color = color
                current_label = label
                current_lines = []

            elif line == "]":
                self.schedule.add_person(current_label, current_color, current_lines)

                current_label = None
                current_color = None
                current_lines = []

            else:
                current_lines.append(self.parse_line(line))

    def parse_line(self, line):
        weekday, start, end, label = line.split("|")
        return self.schedule.create_entry(weekday, start, end, label)
