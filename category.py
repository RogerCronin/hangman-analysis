from parse import parseRuns, parseWords
import matplotlib.pyplot as plt

data = parseRuns()
words = parseWords()
categories = {}

def titler(string):
    return string.title()[0:3]

for word in words:
    if word["hint"] not in categories:
        categories[word["hint"]] = []

for run in data:
    categories[words[run[0]]["hint"]].append(run[1])

for k in categories.keys():
    categories[k] = sum(categories[k]) / len(categories[k])

left = list(range(0, 31))
height = list(categories.values())
labels = list(map(titler, categories.keys()))

plt.bar(left, height, tick_label = labels, width = 0.8)
plt.xlabel("Category")
plt.ylabel("Average difficulty score")
plt.title("Average difficulty of categories")
plt.show()