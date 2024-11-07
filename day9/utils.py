AOC_YEAR = 2023
AOC_URL = "https://adventofcode.com/{year}/day/{day}/input"

from os import getcwd, path, getenv
import sys


def download_input_file():
    '''make URL path and download.'''

    cwd = sys.path[0]
    outfile_path = path.join(cwd, 'input')

    aoc_day = path.split(cwd)[-1]
    daynum = aoc_day.replace('day', '')
    aoc_input_url = AOC_URL.format(year=AOC_YEAR, day=daynum)

    print(f"  Downloading: {aoc_input_url}")
    download_from_url(aoc_input_url, outfile_path)
    print(f"  Downloaded input to: {outfile_path}")

def download_from_url(url, outfile_path):

    from urllib.request import Request, urlopen

    # cookie loaded via Makefile
    SESSION_COOKIE = getenv("AOC_SESSION_COOKIE")
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    request = Request(url, headers=headers)
    try:
        with urlopen(request) as response, open(outfile_path, 'wb') as outfile:
            outfile.write(response.read())
    except Exception as e:
        raise Exception(f"{e}\n---\nERROR: Could not download INPUT file.")
        


def load_input_file():

    input_file_path = path.join(sys.path[0], 'input')
    if not path.exists(input_file_path):
        download_input_file()

    with open(input_file_path) as f:
        data = f.readlines()
    return data



