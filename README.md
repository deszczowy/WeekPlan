# WeekPlan - Weekly Schedule Generator
<img align="right" src="/res/wp.png" width="200"> WeekPlan is a Python script for generating ready to print graphical weekly schedules from user-defined activities. Similar to a school timetable, it allows you to organize virtually any type of activities into a clear, visual weekly plan.

The application runs as a Python script and requires an input file describing the activities to be scheduled.

> **Note:** A standalone executable version is planned for a future release.

Version 1.1

## Table of Contents
- [Requirements and installation](#requirements-and-installation)
- [Basic usage](#basic-usage)
- [Input File Format](#input-file-format)
- [Command-Line Arguments](#command-line-arguments)
- [Examples](#examples)
- [Standalone Version](#standalone-version)
- [Change Log](#change-log)
- [License](#license)

## Requirements and installation
You only need Python 3.x, no additional dependencies are required, so tu use the script:

1. Install Python 3.x if it is not already installed.
2. Clone this repository or download the source code.
3. Open a terminal in the project directory.
4. Create virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```
5. Install required packages.

```bash
python -m pip install -r requirements.txt
```
And You are good to go.

### Building executable
If Python script packed into on executable file is prefered, build it yourself using tools of your choice, or You can use provided script, which uses `pyInstaller` to build executable.

1. Add execution priviledges to the script `chmod +x build.sh`
2. Run `./build.sh`

Result executable will appear in `dist/` directory.

## Basic usage
Run the script from a terminal using the following command:

```bash
python weekplan.py <input_file>
```

Where `<input_file>` is the path to the file describing the weekly plan. In the result script will create `<input_file>.png` file with your weekly plan.

In example:

```bash
python weekplan.py plan.txt
```
will generate `plan.png` file next to the `plan.txt` file.

The input file must follow the structure and formatting rules described in the [Input File Format](#input-file-format) section.

## Input File Format
The input file is a flat text file which defines the title of the weekly plan, the people included in the schedule, and their activities.

### File Structure
The file consists of the following elements:

1. **Plan title** — the first line contains the title of the weekly plan.
2. **Person definitions** — each person is defined in a separate block containing their name, display color, and list of activities.

Each person block is enclosed in square brackets, and starts with a color and a person name. The color is specified as a hexadecimal RGB value prefixed with `#`. Color and name are separated by vertical bar (`|`) character.

Each activity is defined on a separate line using the following format:

```text
DAY|START_TIME|END_TIME|ACTIVITY_NAME
```

Where:

| Field | Description | Example |
|---|---|---|
| `DAY` | Abbreviation of the day of the week. | `MO` |
| `START_TIME` | Activity start time in `HHMM` format. | `800` |
| `END_TIME` | Activity end time in `HHMM` format. | `1045` |
| `ACTIVITY_NAME` | Name or description of the activity. | `Gymnastics` |

Time values use the 24-hour clock without a colon separator. Hours and minutes are written consecutively. For example, `800` represents 08:00, `845` represents 08:45, and `1430` represents 14:30. No leading `0` is required for morning hours.

The color defined for a person is used to identify that person's activities in the generated schedule.

### Example
```text
Weekly Plan
[#7CB4EF|Person 1
MO|800|845|Gym
WE|855|940|Team meeting
]
[#AAFF00|Person 2
MO|1800|1900|Painting class
FR|1055|1140|Dance!
]
```

In this example, the plan contains two people, each assigned a different color. This is just basic overview of activities file. See the `example.txt` file provided with aplication for more details.

### Formatting Rules
- The first line must contain the plan title.
- Each person must be defined in a separate block.
- A person block must start with `[` followed by the hexadecimal color code, a `|` separator, and the person's name.
- Each person block must end with `]` on a separate line.
- Each activity must be defined on a separate line inside the corresponding person block.
- Activity fields must be separated by vertical bars (`|`).
- Time values must use the 24-hour clock without a colon separator.
- Activity names may contain spaces.
- Each activity must specify a day, start time, end time, and activity name.

Week days symbols are:
- **MO** - monday
- **TU** - tuesday
- **WE** - wednesday
- **TH** - thursday
- **FR** - friday
- **SA** - saturday
- **SU** - sunday

Activities can be listed in any order - the script will place them right.

### Validation
The provided file will be checked for correct structure and data, so any errors will be described and marked, which will help create the file correctly.

## Command-Line Arguments
The script supports the following command-line arguments:

| Argument | Short | Description |
|---|---|---|
| `--output` | `-o` | Specify the output file name. |
| `--logfile` | `-l` | Specify the log file name. |
| `--talk` | `-t` | Determines the level of verbosity. Default value is `normal`. Other possible values are: `none`, `info` and `debug`. |
| `--sort` | `-s` | Detemines the sorting order of persons from input file, by their names. Default value is 'original. Other possible values are `az` for ascending order and `za` for descending order. |
| `--position` | `-p` | Place schedule title to the left or right on print (`left` and `right` values) or completly hidden (`hidden` value). Default is `left`.|
| `--help` | `-h` | Display help information and exit. |
| `--version` | `-v` | Display the application version and exit. |

## Examples
Generate a weekly schedule using an input file and default configuration:

```bash
python weekplan.py plan.txt
```

Generate a schedule and specify an output filename:

```bash
python weekplan.py plan.txt --output school-plan
```

## Standalone Version
A standalone executable version is planned for a future release. It will allow users to run the application without installing Python separately.

Until then, Python 3.x is required to run the script.

## Change Log
Current version is 1.1.

### Ver. 1.1
* Schedule title can be placed on the sides of a print or be hidden with `--position` option.
* Person sorting method can be provided with `--sort` parameter.
* Documentation updated

## License
WeekPlan is licensed under the MIT license, so go ahead and do whatever You want with this code. Enjoy!