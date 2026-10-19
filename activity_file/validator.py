import re
from .defaults import *

class Rule:
    def __init__(self, symbol, line, message):
        self.symbol = symbol
        self.line = line
        self.message = message
    
    def to_string(self) -> str:
        return "{0} at line {1}: {2}".format(self.symbol, self.line, self.message)

class Validator:
    """Validates the structure and content of the weekly plan file."""

    # [#RRGGBB|any text
    HEADER_PATTERN = re.compile(r"^\[#[0-9A-Fa-f]{6}\|(.*)$")

    # 1-4 digits
    NUMBER_PATTERN = re.compile(r"^\d{1,4}$")

    def validate(self, lines: list[str]) -> list[str]:
        """
        Validates list of the file lines.
        Result list contains set of broken rules.
        Empty result means data are correct.
        """
        errors = []

        if not lines:
            return [Rule("S01", 0, "File is empty")]

        first_line = lines[0].strip()
        if not first_line:
            errors.append(Rule("S02", 1, "Title can not be empty"))

        if first_line.startswith("["):
            errors.append(Rule("S03", 1, "File should start with a title, not a person schedule"))
        inside_block = False

        for line_number, line in enumerate(lines[1:], start=2):
            # Person schedule start
            if line.startswith("["):
                if inside_block:
                    errors.append(Rule("S04", line_number, "Persons schedules can not be nested"))
                    continue

                if not self.HEADER_PATTERN.fullmatch(line):
                    errors.append(Rule("S05", line_number, "Incorrect persons schedule header"))
                    continue

                inside_block = True
                continue

            # Person schedule end
            if line == "]":
                if not inside_block:
                    errors.append(Rule("S06", line_number, "Unexpected schedule closing before opening"))
                    continue

                inside_block = False
                continue

            # Entries can not be outside of a schedule
            if not inside_block:
                errors.append(Rule("S07", line_number, "Schedule entry outside of schedule"))
                continue

            # Walidacja wpisu
            errors.extend(self._validate_entry(line, line_number))

        if inside_block:
            errors.append(Rule("S07", len(lines), "Unexpected end of file (no closing symbol found)"))

        return errors

    def _validate_entry(
        self,
        line: str,
        line_number: int,
    ) -> list[str]:
        errors = []

        fields = line.split("|")
        count = len(fields)

        if count != ENTRY_FIELDS_COUNT:
            return [
                Rule("E01", line_number, "Entry has to have {0} fields separated by |, but {1} found".format(ENTRY_FIELDS_COUNT, count))
            ]

        day, start, end, description = fields

        # Week day
        if day not in DAYS:
            errors.append(Rule("E02", line_number, f"Incorrect weekday symbol, {day!r} found."))

        # Start time
        if not self.NUMBER_PATTERN.fullmatch(start):
            errors.append(Rule("E03", line_number, f"Incorrect time format, {start!r}."))

        # End time
        if not self.NUMBER_PATTERN.fullmatch(end):
            errors.append(Rule("E03", line_number, f"Incorrect time format, {end!r}."))

        # Description
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(Rule("E04", line_number, "Entry description too long, {0} > {1}".format(count, MAX_DESCRIPTION_LENGTH)))

        return errors