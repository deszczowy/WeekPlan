# Command-Line Interface

[Back to README](../README.md)

Basic script call only requires the path to the activity file.

```bash
python weekplan.py <input_file>

weekplan <input_file>
```

The script will then create a printout using the default settings. There are commands available to extend the capabilities of standard processing as well as several helpful switches.

From now on, I will use standalone application calls in documentation examples.

### Help
```
--help
-h
```
Display help information and exit. Although I try to keep the documentation always up to date, you can get a most current description of available commands via this switch.

### Script version
```
--version
-v
```
Display the application version and exit.

### Output file name

```
--output
-o
```
By default script will take the input file name and use it to name a `png` file with schedule print. With this option You can specify the output file name - just a name, script will add proper extension.

Below example will produce `schedule-print.png` file, instead of default `my-plan.png`.

```bash
weekplan my-plan.txt --output schedule-print
```

### Logging destination file

```
--logfile
-l
```
Main output channel is command line, but you may want to save output on disk. Use this command to point to the log file. If the file does not exist, the script will create it. If the file exists, script output will be added to it (the existing content will not be ereased).

### Script verbosity

```
--talk
-t
```
This parameter controls script verbosity level. Possible values are:

|Value|Description|
|---|---|
|`none`|Script will run completly silent|
|`normal`|Greeting, processing stages confirmations, file validation notices|
|`debug`|Normal level notices plus additional processing messages usefull mainly for error analyze|
|`info`| Debug level notices plus every other additional messages left in script, human readable or not|

Default is `normal`.

### Persons schedules sorting order

```
--sort
-s
```
Detemines the sorting order for persons from the activity file. Sorting is done by person's name and affects the order in which people appear on the printout - in the daily activity diagram and in the schedule description.

|Value|Description|
|---|---|
|`original`|Persons are added to the printout as they appears in activity file|
|`az`|Persons will be sorted in ascending order|
|`za`|Persons will be sorted in descending order|

Default is `original`.

### Title position

```
--position
-p
```
The schedule title is printed just below the weekly activity chart. You can decide where to place it or to hide it completely.


|Value|Description|
|---|---|
|`left`|Title will be left aligned|
|`right`|Title will be right aligned|
|`hidden`|Don't print schedule title at all|

Default is `left`.