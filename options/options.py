from .enum_log import LogLevel
from .enum_sort import SortOrder
from .tool import Tool


class Options:

    def __init__(self) -> None:
        # Schedule
        self.sort_order: SortOrder = SortOrder.ORIGINAL

        # Logging
        self.log_file: str = None
        self.log_level: LogLevel = LogLevel.JUST_COMMUNICATION

        # I/O
        self.input_file_name: str = None
        self.output_file_name: str = None
    
    def set_io(self, input_file, output_file) -> None:
        self.input_file_name = input_file
        self._set_output_file(output_file)

    def _set_output_file(self, output_file) -> None:
        output = output_file
        if output is None:
            output = self.input_file_name
        self.output_file_name = Tool.change_extension(output, "png")
