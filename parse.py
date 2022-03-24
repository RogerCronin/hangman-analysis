import json

def parseRuns():
    content = open("db.txt", "r").read()
    content = content.split()
    data = []
    for run in content:
        run = run.split(";")
        run[0] = int(run[0])
        run[1] = float(run[1])
        data.append(run)
    return sorted(data, key = lambda x: x[1])

def parseWords():
    content = json.load(open("words.json"))
    return content["words"]