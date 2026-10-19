from planner import Schedule


class FileReader:
    def __init__(self, file_path, schedule, logger):
        self.schedule = schedule
        self.schedule.header = ""
        self.schedule.data = {}

        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file]

        if lines:
            self.schedule.header = lines[0]
            logger.notice("Reading \"{0}\".".format(self.schedule.header))

        current_label = None
        current_color = None
        current_lines = []

        for line in lines[1:]:
            if line.startswith("["):
                # [00FFAA|etykieta1
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
