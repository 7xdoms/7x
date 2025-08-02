import os
import sys
import importlib
import subprocess
import webbrowser

libraries_to_install = [
    "requests", "mechanize", "names", "render", "user_agent", "telethon",
    "python-cfonts", "pyfiglet", "colorama", "random", "types", "rich", "uuid",
    "time", "string", "secrets", "bs4", "json", "socket", "pysocks", 
    "pycryptodome"
]


for library in libraries_to_install:
    try:
        importlib.import_module(library)
        print(f"  \x1b[2;32m{library} is already installed ✅ ")
    except ImportError:
        print(f"\x1b[2;31m{library} not installed. Installing... ❌")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])


for package in libraries_to_install:
    try:
        __import__(package.replace("-", "_").replace("python_", ""))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

