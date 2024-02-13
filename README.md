# Batch renamer

A platform-agnostic file renaming app made in Python, intended to replicate MacOS file batch renaming functionality for Windows.

User must input base filename, and the app will rename files to filename-#.ext format.


## Dependencies

- Python 3.12.1
- Pip 24.0
- Pyinstaller 6.4.0

## Install

```
python -m venv venv #comment
.\venv\Scripts\activate (win)
source venv/bin/activate (mac)
pip install pyinstaller
pyinstaller --onefile --noconsole main.py

```

## Usage

Run dist/filerenamer.exe

## License

MIT © Rihards Rudzitis
