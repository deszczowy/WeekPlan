import argparse
from logger import LogLevel

class WeekPlan:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Generating printable activities week plan."
        )

        parser.add_argument(
            "INPUT",
            type=str,
            help="Path to file with activities description."
        )

        parser.add_argument(
            "-o", "--output",
            type=str,
            nargs="?",
            default=None,
            help="Name of an output file. Optional, if not provided, input file name will be used."
        )

        parser.add_argument(
            "-l", "--logfile",
            type=str,
            nargs="?",
            help="Name of a file where app log will be stored, beside the default console output."
        )
        
        parser.add_argument(
            "-t", "--talk",
            type=str,
            choices=["none", "normal", "info", "debug"],
            nargs="?",
            default="normal",
            help="Provide custom level of app communication log."
        )

        parser.add_argument(
            "-v", "--version",
            action="version",
            version="%(prog)s is 1.0",
        )

        self.args = parser.parse_args()

    def execute(self):

        print(self.args)

        if self.args.INPUT is not None:

            # Input file was provided - proceed:
            log_level = self._get_log_level(self.args.talk)

            from wrapper import Wrapper
            Wrapper(
                self.args.INPUT,
                self.args.output,
                self.args.logfile,
                log_level
            )
    
    def _get_log_level(self, input: str) -> LogLevel:
        if input == "none":
            return LogLevel.SILENT
        if input == "debug":
            return LogLevel.ALSO_DEBUG
        if input == "info":
            return LogLevel.EVEN_INFO
        return LogLevel.JUST_COMMUNICATION