# File renamer

A platform-agnostic file renaming app made in Python, intended to replicate MacOS file batch renaming functionality for Windows.

User must input folder directory, base filename, desired counter start value, and the app will rename all files in a folder to filename-#.ext format.

## Dependencies

- Python 3.12.1
- Pyinstaller 6.4.0

## Install

1. Install Python 
2. Create environment
```
python -m venv venv
```
3. Activate environment
```
.\venv\Scripts\activate (win)
source venv/bin/activate (mac)
```
4. Install Pyinstaller
```
pip install pyinstaller
```
5. Generate executable
```
pyinstaller --onefile --noconsole main.py
```

## Usage

You can just grab the .exe file inside 'dist' folder and run that, if you don't want to deal with generating the executable yourself.

## License

MIT © Rihards Rudzitis