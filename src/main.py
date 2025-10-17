import sys
from fetch_user_info import *

arguments = sys.argv[1:]
if len(arguments) == 0:
    print("Usage: uv run main.py <target_username>")
    sys.exit(0)
elif len(arguments) > 1:
    print("Too many arguments given.")
    sys.exit(1)

fetch_user_info(*arguments)
