from .enum_log import LogLevel
from .enum_sort import SortOrder


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
        self.output_file_name = self.change_extension(output, "png")

    # -> General tool
    def change_extension(self, file_path: str, new_extension: str) -> str:
        from pathlib import Path
        
        path = Path(file_path)
        new_extension = new_extension.lstrip(".")
        new_path = path.with_suffix(f".{new_extension}")
        return str(new_path)