import sys
from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your Python script
script = 'main.py'


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'packages': ['tkinter', 'tkinter.messagebox', 'browse','time','random','selenium'], 
    'include_files': ['youtube.ico',]
    }

# GUI applications require a different base on Windows (the default is for a console application).
base = None

exe = Executable(script, base=base)

setup(
    name='Get YouTube Views',
    version='1.0',
    description='Get YouTube Views',
    options={'build_exe': build_exe_options},
    executables=[exe]
    )
        

# Run the command 'python setup.py build' to build the executable.

