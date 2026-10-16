import argparse


class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Generating printable activities week plan."
        )

        parser.add_argument(
            "INPUT",
            type=str,
            help="Path to file with activities description. Required."
        )

        parser.add_argument(
            "OUTPUT",
            type=str,
            nargs="?",
            default=None,
            help="Name of an output file. Optional, if not provided, input file name will be used."
        )

        self.args = parser.parse_args()

    def execute(self):

        if self.args.INPUT is not None:
            from wrapper import Wrapper
            Wrapper(self.args.INPUT, self.args.OUTPUT)

if __name__ == "__main__":
    cli = CLI()
    cli.execute()