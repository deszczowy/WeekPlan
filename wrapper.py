from planner import Schedule
from activity_file import Parser
from plan import Plan
from logger import Logger, LogLevel

        
class Wrapper:

    def __init__(self, input_file, output_file, log_file, log_level) -> None:
        
        self.input_file_name = input_file
        self.output_file_name = self.get_output_file(output_file)

        # Notification surface
        logger = Logger(log_level, log_file)
        
        # Base schedule
        shedule = Schedule()

        # Reading input file
        result = Parser(input_file, shedule, logger).parse()

        if result is True:
            # Generating week plan print
            Plan(self.output_file_name, shedule)
    
    def get_output_file(self, output_file) -> str:
        output = output_file
        if output is None:
            output = self.input_file_name
        output = self.change_extension(output, "png")
        return output

    # -> General tool
    def change_extension(self, file_path: str, new_extension: str) -> str:
        from pathlib import Path
        
        path = Path(file_path)
        new_extension = new_extension.lstrip(".")
        new_path = path.with_suffix(f".{new_extension}")
        return str(new_path)