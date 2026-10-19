from planner import Schedule


class FileReader:
    def __init__(self, file_path, schedule, logger):
        self.schedule = schedule
        self.schedule.clear()
        self.file = file_path
        self.logger = logger
        self.lines = []
        self.process()

    def process(self) -> None:
        self.get_file_lines()
        if self.lines:
            self.set_header()
            self.set_data()
        else:
            self.logger.notice("No data in provided file was found.")
    
    def get_file_lines(self) -> None:
        self.lines = []
        with open(self.file, "r", encoding="utf-8") as file:
            self.lines = [line.strip() for line in file]
    
    def set_header(self) -> None:
        self.schedule.header = self.lines[0]
        self.logger.notice("Reading \"{0}\".".format(self.schedule.header))

    def set_data(self) -> None:
        current_label = None
        current_color = None
        current_lines = []

        for line in self.lines[1:]:
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
