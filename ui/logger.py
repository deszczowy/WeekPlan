import os
from options import Options, LogLevel
 
class Logger:

    def __init__(self, options: Options) -> None:
        self.level = options.log_level
        self.file = options.log_file

    def info(self, message: str) -> None:
        if self.level == LogLevel.EVEN_INFO:
            self.show(message)

    def debug(self, message: str) -> None:
        if self.level.value >= LogLevel.ALSO_DEBUG.value:
            self.show(message)
    
    def notice(self, message: str) -> None:
        if self.level.value >= LogLevel.JUST_COMMUNICATION.value:
            self.show(message)
    
    def show(self, message: str) -> None:
        print(message)
        if self.file is not None:
            self.store(message)
    
    def store(self, message: str) -> None:
        try:
            with open(self.file, "a", encoding="utf-8") as log:
                log.write("{}\n".format(message))
        except Exception as e:
            print("Error while writing to log file: {0}".format(e))


"""
l = Logger(LogLevel.EVEN_INFO, "test.log")
l.info("This is info")
l.debug("This is debug")
l.notice("This is basic notice")
"""
