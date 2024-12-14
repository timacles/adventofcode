AOC_YEAR = 2024
AOC_URL = "https://adventofcode.com/{year}/day/{day}/input"


from os import getcwd, path, getenv, listdir, mkdir
import sys
import logging as log
from shutil import copyfile


log.basicConfig(
    level=log.DEBUG,
    format="%(levelname)s - %(message)s",
    handlers=[log.StreamHandler()],
)

debug = log.debug
info = log.info


def load_input_file(day_module_path):
    """load the input, download if it doesnt exist"""
    day_id, day_dir = parse_day_module_path(day_module_path)
    input_file_path = path.join(day_dir, "input")
    # download if file no existy
    if not path.exists(input_file_path):
        cwd = day_module_path
        outfile_path = path.join(cwd, "input")
        aoc_day = path.split(cwd)[-1]
        daynum = aoc_day.replace("day", "")
        aoc_input_url = AOC_URL.format(year=AOC_YEAR, day=daynum)
        print(f"  Downloading: {aoc_input_url}")
        download_from_url(aoc_input_url, outfile_path)
        print(f"  Downloaded input to: {outfile_path}")
    with open(input_file_path) as f:
        data = f.read()
    return data


def download_from_url(url, outfile_path):

    from urllib.request import Request, urlopen
    from dotenv import load_dotenv

    load_dotenv()

    # cookie loaded via Makefile
    SESSION_COOKIE = getenv("AOC_SESSION_COOKIE")
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    request = Request(url, headers=headers)
    try:
        with urlopen(request) as response, open(outfile_path, "wb") as outfile:
            outfile.write(response.read())
    except Exception as e:
        raise Exception(f"{e}\n---\nERROR: Could not download INPUT file.")


def parse_day_module_path(filepath):
    day_dir = path.dirname(filepath)
    day_id = path.basename(day_dir)
    return day_id, day_dir


def initialize_day_module(day):
    ''' initialize a day solver module '''
    new_day_path = path.join(sys.path[0], 'day' + day)

    # exit if day already exists
    if path.exists(new_day_path):
        print(f"  DAY {day} ALREADY EXISTS. exiting ... ")
        return

    print(f"  initializing module for day {day}.   {new_day_path}")
    mkdir(new_day_path)
    for directory, filename in get_list_of_template_files():
        template_file_path = path.join(directory, filename)
        init_file = filename.strip('tmpl.')
        new_init_path = path.join(new_day_path, init_file)
        if path.exists(new_init_path):
            raise Exception(f"{new_init_path} already exists")
        #ecopyfile(template_file_path, new_init_path)
        print(template_file_path, new_init_path)


def get_list_of_template_files():
    files = []
    directory = sys.path[0]
    template_dir = path.join(directory, 'templates')
    for filename in listdir(template_dir):
        if filename.startswith('tmpl.'):
            files.append((template_dir, filename,))
    return files