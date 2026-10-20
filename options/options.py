from .enum_log import LogLevel
from .enum_sort import SortOrder
from .enum_position import TitlePosition
from .tool import Tool
from .consts import TALK_MAPPER, SORT_MAPPER, TITLE_POSITION_MAPPER


class Options:

    def __init__(self) -> None:
        # Schedule
        self.sort_order: SortOrder = SortOrder.ORIGINAL
        self.title_position: TitlePosition = TitlePosition.LEFT

        # Logging
        self.log_file: str = None
        self.log_level: LogLevel = LogLevel.JUST_COMMUNICATION

        # I/O
        self.input_file_name: str = None
        self.output_file_name: str = None
    
    def update(self, args: Namespace) -> None:
        self._set_io(args.input, args.output)
        self._set_log(args.talk, args.logfile)
        self._set_printer(args.sort, args.position)

        if self.log_level == LogLevel.ALSO_DEBUG:
            print(args)
    #
    # Setup
    #
    def _set_io(self, input_file: str, output_file: str) -> None:
        self.input_file_name = input_file
        self._set_output_file(output_file)
    
    def _set_log(self, log_level_name: str, log_file: str) -> None:
        self._set_log_level(log_level_name)
        self.log_file = log_file
    
    def _set_printer(self, sort_order: str, position: str) -> None:
        self._set_sort_order(sort_order)
        self._set_title_position(position)

    #
    # Mappers
    #
    def _set_log_level(self, input: str) -> None:
        if input in TALK_MAPPER.keys():
            self.log_level = TALK_MAPPER[input]
        else:
            self.log_level =  LogLevel.JUST_COMMUNICATION
    
    def _set_sort_order(self, input: str) -> None:
        if input in SORT_MAPPER.keys():
            self.sort_order = SORT_MAPPER[input]
        else:
            self.sort_order = SortOrder.ORIGINAL
    
    def _set_title_position(self, input: str) -> None:
        if input in TITLE_POSITION_MAPPER.keys():
            self.title_position = TITLE_POSITION_MAPPER[input]
        else:
            self.title_position = TitlePosition.LEFT

    def _set_output_file(self, output_file) -> None:
        output = output_file
        if output is None:
            output = self.input_file_name
        self.output_file_name = Tool.change_extension(output, "png")
