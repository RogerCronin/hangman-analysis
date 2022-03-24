from parse import parseRuns, parseWords
import matplotlib.pyplot as plt

data = parseRuns()
words = parseWords()

def plotLetter(letter):

    scores = {
        "0.0": [],
        "0.1": [],
        "0.2": [],
        "0.3": [],
        "0.4": [],
        "0.5": [],
        "0.6": [],
        "0.7": [],
        "0.8": [],
        "0.9": [],
        "1.0": []
    }

    for run in data:
        word = words[run[0]]["word"]
        scores[str(run[1])].append(word.count(letter))

    for k in scores.keys():
        if len(scores[k]) == 0:
            continue
        scores[k] = sum(scores[k]) / len(scores[k])

    xAxis = list(map(lambda x: float(x), scores.keys()))
    yAxis = list(scores.values())
    yAxis[5] = (yAxis[4] + yAxis[6]) / 2

    plt.plot(xAxis, yAxis, label = letter.upper() + " occurrences")

plotLetter("a")
plotLetter("e")
plotLetter("i")
plotLetter("o")
plotLetter("u")
plotLetter("y")
plt.xlabel("Difficulty score")
plt.ylabel("Average letter frequency")
plt.title("Average frequency of vowels compared to difficulty")
plt.legend()
plt.show()