from entry import Entry
from person import Person


class FileReader:
    def __init__(self, file_path, week_plan, logger):
        week_plan.header = ""
        week_plan.data = {}

        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file]

        if lines:
            week_plan.header = lines[0]
            logger.notice("Reading \"{0}\".".format(week_plan.header))

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
                week_plan.data[current_label] = Person(
                    name=current_label,
                    color=current_color,
                    lines=current_lines
                )

                current_label = None
                current_color = None
                current_lines = []

            else:
                current_lines.append(self.parse_mo_line(line))

    def parse_mo_line(self, line):
        weekday, start, end, label = line.split("|")
        return Entry(
            weekday=weekday,
            start=start,
            end=end,
            label=label
        )
