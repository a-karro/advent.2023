import urllib.request
import os

SAMPLE = -1


def __load_dotenv():
    try:
        with open("./.env", "r") as env:
            res = {}
            lines = env.read().splitlines()
            for line in lines:
                k, v = line.split("=")
                res[k] = v
            return res
    except Exception as e:
        print(e)
        return None


def retriever(year, day):
    if not (env := __load_dotenv()):
        raise RuntimeError("Could not load environment!")

    if day == SAMPLE:
        if not os.path.isfile("data/sample.txt"):
            with open("data/sample.txt", "w") as f:
                f.write("Paste the sample from AoC you're solving in data/sample.txt\n")
        return open("data/sample.txt", "r")

    filename = f"data/day{day:02d}.txt"
    if not os.path.isfile(filename):
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        req = urllib.request.Request(url)
        req.add_header("Cookie", f"session={env['AOC_SESSION']}")
        data = urllib.request.urlopen(req).read()
        with open(filename, "wb") as f:
            f.write(data)
    f = open(filename, "r")
    return f
