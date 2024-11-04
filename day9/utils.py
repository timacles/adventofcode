AOC_YEAR = 2023
AOC_URL = "https://adventofcode.com/{year}/day/{day}/input"

from os import getcwd, path, getenv
import sys

SESSION_COOKIE = getenv("AOC_SESSION_COOKIE")

def download_input_file():
    '''make URL path and download.'''

    cwd = sys.path[0]
    outfile_path = path.join(cwd, 'input')

    aoc_day = path.split(cwd)[-1]
    daynum = aoc_day.replace('day', '')
    aoc_input_url = AOC_URL.format(year=AOC_YEAR, day=daynum)

    from urllib.request import urlretrieve
    
    print(f"  Downloading: {aoc_input_url}")
    urlretrieve(aoc_input_url, outfile_path)
    print(f"  Downloaded input to: {outfile_path}")
    
def load_file(f):
    with open(f) as f:
        data = f.readlines()
    return data



