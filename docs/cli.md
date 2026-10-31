## Command-Line Arguments
The script supports the following optional command-line arguments:

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
