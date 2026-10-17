import argparse


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
            "-v", "--version",
            action="version",
            version="%(prog)s is 1.0",
        )

        self.args = parser.parse_args()

    def execute(self):

        print(self.args)
        if self.args.INPUT is not None:
            from wrapper import Wrapper
            Wrapper(self.args.INPUT, self.args.output)