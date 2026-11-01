# Installation and build

[Back to README](../README.md)

### Requirements and installation

You only need Python 3.x to use the script:

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
And You are good to go. Run version check to verify if script is working.

```bash
python weekplan.py --version
```

### Building executable

If you prefer to use a built executable instead of a script, you can create it with tools of your choice, but you can also use the provided bash script, which uses `pyInstaller`.

1. Add execution priviledges to the script `chmod +x build.sh`
2. Run `./build.sh`

Result executable will appear in `dist/` directory.
