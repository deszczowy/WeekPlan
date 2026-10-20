from .enum_log import LogLevel
from .enum_sort import SortOrder

# Weekdays symbols
WEEKDAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

TALK_MAPPER = {
    "none": LogLevel.SILENT,
    "normal": LogLevel.JUST_COMMUNICATION,
    "debug": LogLevel.ALSO_DEBUG,
    "info": LogLevel.EVEN_INFO,
}

SORT_MAPPER = {
    "original": SortOrder.ORIGINAL,
    "az": SortOrder.A_TO_Z,
    "za": SortOrder.Z_TO_A,
}