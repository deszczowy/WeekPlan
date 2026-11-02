from .enum_log import LogLevel
from .enum_sort import SortOrder
from .enum_position import TitlePosition
from .enum_range import WeekDaysRange

# Weekdays symbols
WEEKDAYS = {
    "MO": "MO",
    "TU": "TU",
    "WE": "WE",
    "TH": "TH",
    "FR": "FR",
    "SA": "SA",
    "SU": "SU"
}

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

TITLE_POSITION_MAPPER = {
    "hidden": TitlePosition.HIDDEN,
    "left": TitlePosition.LEFT,
    "right": TitlePosition.RIGHT,
}

WEEKDAYS_RANGE_MAPPER = {
    "workdays": WeekDaysRange.WORKDAYS,
    "weekend": WeekDaysRange.WEEKEND,
    "active": WeekDaysRange.ACTIVE,
    "scope": WeekDaysRange.SCOPE,
    "all": WeekDaysRange.ALL
}