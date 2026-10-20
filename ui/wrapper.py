from planner import Schedule
from activity_file import Parser
from painter import Plan
from options import Options

from .logger import Logger

        
class Wrapper:

    def __init__(self, options: Options) -> None:

        # Notification surface
        logger = Logger(options)
        
        # Base schedule
        shedule = Schedule()

        # Reading input file
        result = Parser(options, shedule, logger).parse()

        if result is True:
            # Generating week plan print
            Plan(options, shedule, logger)
            logger.notice("Week plan saved in {0}".format(options.output_file_name))