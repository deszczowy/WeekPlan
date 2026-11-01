# WeekPlan - Weekly Schedule Generator

<img align="right" src="/res/wp.png" width="200"> WeekPlan is a Python script for generating ready to print graphical weekly schedules from user-defined activities. Similar to a school timetable, it allows you to organize virtually any type of activities into a clear, visual weekly plan.

Latest version is 1.3

## Documentation
- [Installation](docs/build.md)
- [Command-Line inteface options](docs/cli.md)
- [Activity File structure description](docs/file.md)

## Overview

See [installation](docs/build.md) instruction to prepare the script, then run it from a terminal using the following command:

```bash
python weekplan.py <input_file>
```

Where `<input_file>` is the path to the file describing the weekly plan. In the result script will create `<input_file>.png` file with your weekly schedule print.

In example:

```bash
python weekplan.py plan.txt
```
will generate `plan.png` file next to the `plan.txt` file.

The input file must follow the structure and formatting rules described in the [Activity File structure documentation](docs/file.md).


## Change Log

### Ver. 1.3
* Adding background picture to schedule print.
* Documentation updated.

### Ver. 1.2
* Weekday names aliases now can be provided from an activity file.
* Documentation updated.

### Ver. 1.1
* Schedule title can be placed on the sides of a print or be hidden with `--position` option.
* Person sorting method can be provided with `--sort` parameter.
* Documentation updated.

## License
WeekPlan is licensed under the MIT license, so go ahead and do whatever you want with this code. Enjoy!