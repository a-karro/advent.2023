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
    except:  # noqa
        return None


def retriever(year, day):
    env = __load_dotenv()

    if day == SAMPLE:
        if not os.path.isfile("data/sample.txt"):
            with open("data/sample.txt", "w") as f:
                f.write("Paste the sample from AoC you're solving in data/sample.txt\n")
        return open("data/sample.txt", "r")

    filename = f"data/day{day:02d}.txt"
    if not os.path.isfile(filename):
        if env:
            url = f"https://adventofcode.com/{year}/day/{day}/input"
            req = urllib.request.Request(url)
            req.add_header("Cookie", f"session={env['AOC_SESSION']}")
            data = urllib.request.urlopen(req).read().decode()
            if data[-1] == "\n":
                data = data[:-1]
        else:
            data = f"Get the input data for Day {day} from AoC and save as {filename}"
        with open(filename, "w") as f:
            f.write(data)
    f = open(filename, "r")
    return f
