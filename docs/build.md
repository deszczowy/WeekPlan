# Installation and build

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
