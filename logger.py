from enum import Enum

class LogLevel(Enum):
    EVEN_INFO = 3
    ALSO_DEBUG = 2
    JUST_COMMUNICATION = 1
    SILENT = 0
 
class Logger:

    def __init__(self, level: LogLevel) -> None:
        self.level = level

    def info(self, message: str) -> None:
        if self.level == LogLevel.EVEN_INFO:
            print(message)

    def debug(self, message: str) -> None:
        if self.level.value >= LogLevel.ALSO_DEBUG.value:
            print(message)
    
    def notice(self, message: str) -> None:
        if self.level.value >= LogLevel.JUST_COMMUNICATION.value:
            print(message)

"""
l = Logger(LogLevel.SILENT)
l.info("This is info")
l.debug("This is debug")
l.notice("This is basic notice")
"""