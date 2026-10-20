import argparse
from options import Options, LogLevel
from .wrapper import Wrapper

class CommandLine:
    def __init__(self):

        self.description = "Generating printable activities week plan."
        self.version = "1.0"

        self.build_command_line()
        self.parse()        

    def run(self):

        if self.args.input is not None:

            options = Options()
            options.set_io(self.args.input, self.args.output)

            # Input file was provided - proceed:
            log_level = self.get_log_level(self.args.talk)

            if log_level.value >= LogLevel.ALSO_DEBUG.value:
                print(self.args)

            Wrapper(options)
    
    def build_command_line(self) -> None:
        self.build_parser()
        self.add_positional("input", "Path to file with activities description")
        self.add_str("-o", "--output", "Name of an output file. Optional, if not provided, input file name will be used")
        self.add_str("-l", "--logfile", "Name of a file where app log will be stored, beside the default console output")
        self.add_choice("-t", "--talk", ["none", "normal", "info", "debug"], "normal", "Provide custom level of app communication log")
        # self.add_choice("-s", "--sort", ["original", "az", "za"], "original", "Sorting order of people's plans by persons names")
        # self.add_choice("-p", "--position", ["left", "center", "right"], "left", "Position of schedule title on print")
        
        self.add_version()
    
    def parse(self) -> None:
        self.args = self.parser.parse_args()

    def get_log_level(self, input: str) -> LogLevel:
        if input == "none":
            return LogLevel.SILENT
        if input == "debug":
            return LogLevel.ALSO_DEBUG
        if input == "info":
            return LogLevel.EVEN_INFO
        return LogLevel.JUST_COMMUNICATION

    def build_parser(self) -> None:
        self.parser = argparse.ArgumentParser(
            description=self.description
        )
    
    def add_version(self) -> None:
        self.parser.add_argument(
            "-v", "--version",
            action="version",
            version="%(prog)s is " + self.version,
        )
    
    def add_positional(self, name, description) -> None:
        self.parser.add_argument(
            name,
            type=str,
            help=description
        )

    def add_str(self, cshort, clong, description) -> None:
        self.parser.add_argument(
            cshort, clong,
            type=str,
            nargs=1,
            default=None,
            help=description
        )
    
    def add_choice(self, cshort, clong, choices, default, description) -> None:
        self.parser.add_argument(
            cshort, clong,
            type=str,
            choices=choices,
            nargs=1,
            default=default,
            help=description
        )