import os
from urllib.request import Request, urlopen

from dotenv import load_dotenv


def get_input(day, to_lines=True):
    load_dotenv()
    file_name = f"day_{day:02}.txt"
    session_key = os.getenv("AOC_SESSION")
    if not os.path.exists(file_name):
        req = Request(f"https://adventofcode.com/2022/day/{day}/input")
        req.add_header("cookie", f"session={session_key}")
        input = urlopen(req).read()
        with open(file_name, "wb") as f:
            f.write(input)

    with open(file_name) as f:
        if to_lines:
            return f.readlines()
        else:
            return f.read()
