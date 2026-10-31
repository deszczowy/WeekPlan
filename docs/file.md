# Activity File Description

[go back to README](../README.md)

WeekPlan generates prints base on data provided with structured text file, which defines the main title, people included in schedule, and their activities. This document will help You create and maintain your activity file.

## Basic example

Below is basic overview of activity file, which contains definitions of two people and theirs activities, each person has different color assigned to. 

```text
Here is the week plan main title.
{
MO|Monday
WE|Wednesday
FR|Friday
}
[#7CB4EF|Person 1
MO|800|845|Gym
WE|855|940|Team meeting
]
[#AAFF00|Person 2
MO|1800|1900|Painting class
FR|1055|1140|Dance!
]
```
You can find more elaborate, ready to run example in `example.txt` file in root directory, which can also be used as a template.

## File Structure

The file consists of the following elements:

1. Obligatory **Title** stored in file first line.
2. **Weekdays aliases dictionary** where You can define weekdays names aliases in your own language.
3. **Persons activities definitions** where each person is defined in a separate block containing their name, display color, and list of activities.

### Structure rules

* Dictionaries and activities blocks are made up of entries. Each entry occupies one line.
* Entry fields are separated by pipe character `|`.
* Empty line is not a valid line, so it does not count when WeekPlan is parsing file.
* Using comments is supported. Comment is a line which starts from hash character `#`.


### Title

This part is obligatory. It has no length constraint, but remember that it will be printed on a schedule, so schould be possibly short and descriptive.

### Weekdays aliases dictionary

WeekPlan uses this weekdays symbols to determine day of the week in which given activity occurs. Week days symbols are:

- **MO** - monday
- **TU** - tuesday
- **WE** - wednesday
- **TH** - thursday
- **FR** - friday
- **SA** - saturday
- **SU** - sunday

Those symbols are also used to build day column of activities. To print readable headers of days every symbol should be covered with an alias. If a weekday has no alias defined, symbol will be printed. File can have defined only aliases for days used in schedule, as shown in above file example, and that is fine.

Dictionary entries are located between curly brackets, each entry occupies one line and has following format:

```text
DAY_SYMBOL|ALIAS
```

### Person

Each person is defined in a separate block. Person block is enclosed in square brackets. Block definition contains color and name. A color is specified as a hexadecimal RGB value prefixed with `#`.

You can experiment with a value or use any color picker available online.

### Activity

Each activity is an entry, so is a separate line and has the following format:

```text
DAY|START_TIME|END_TIME|ACTIVITY_NAME
```

Where:

| Field | Description | Example |
|---|---|---|
| `DAY` | Week day symbol. | `MO` |
| `START_TIME` | Activity start time| `800` |
| `END_TIME` | Activity end time| `1045` |
| `ACTIVITY_NAME` | Description of the activity. | `Gymnastics` |

Time values use the 24-hour clock in `HHMM` format, without a colon separator. Hours and minutes are written consecutively. Leading `0` can be ommited. For example, `800` represents 08:00, `845` represents 08:45, and `1430` represents 14:30. 

The color defined for a person is used to identify that person's activities in the generated schedule.

Description should be short and descriptive of maximum 100 characters. It can contain all kind of alpha-numerical characters, spaces too, except pipe separator `|`. Activity without description is also a valid entry and will show only hours in generated schedule.

Activities can be listed in any order - the script will place them right.

Activity entry stored outside of a person block is considered error and will cause printing to fail.

## Validation

Before printing file will undergo a validation process. Each found error will be listed in WeekPlan output. Broken rule information will show You rule symbol, number of file line which broke the rule and short decription.

Validation is perform on a "clean" file without empty lines and comments, so keep this in mind when looking for a erroneus line.

All rules are listed below:

| Symbol | Description | Comment |
|---|---|---|
|S01|File is empty|Check if You use proper file or maybe your file contains some white non-alpha-numerical character which could break file processng. |
|S02|Title can not be empty|You miss the title somehow.|
|S03|ile should start with a title, not a person schedule|It is a consequential rule to the S02.|
|S04|Persons schedules can not be nested|-|
|S05|Incorrect persons schedule header|-|
|S06|Person name can not be empty|-|
|S07|Unexpected schedule closing before opening|-|
|S08|Schedule entry outside of schedule|-|
|S09|Unexpected end of file (no closing symbol found)|-|
|S10|Persons schedules can not be placed in a context block.|-|
|E01|Entry has to have X fields, but Y found|-|
|E02|Incorrect weekday symbol, X found|-|
|E03|Incorrect time format|-|
|E04|End time must be later than the start time|-|
|E05|Entry description too long, X > Y|-|