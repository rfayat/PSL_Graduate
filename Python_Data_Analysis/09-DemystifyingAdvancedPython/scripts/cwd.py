"Test script, simply print the current working directory."
from pathlib import Path

cwd = Path.cwd()  # current working directory
print(cwd)