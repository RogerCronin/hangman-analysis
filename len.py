from parse import parseRuns, parseWords
import re
import matplotlib.pyplot as plt

def count(string):
    return len(re.sub(r"\W+", "", string))

data = parseRuns()
words = parseWords()

lengths = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

for run in data:
    word = words[run[0]]["word"]
    lengths[count(word)].append(run[1])

for i in range(0, len(lengths)):
    if len(lengths[i]) == 0:
        continue
    lengths[i] = sum(lengths[i]) / len(lengths[i])

for i in range(0, 6):
    lengths.pop(0)

plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], lengths)
plt.xlabel("Character count")
plt.ylabel("Average difficulty score")
plt.title("Length of words compared to average difficulty")
plt.show()