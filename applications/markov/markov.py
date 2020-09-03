import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

words = words.split()
start_words = []
end_words = []
d = {}

for x in range(len(words) - 1):
    if not d.get(words[x]):
        d[words[x]] = [words[x + 1]]
    else:
        d[words[x]].append(words[x + 1])

for x in words:
    if x[0].isupper():
        start_words.append(x)
    if x == '"' and x[1].isupper():
        start_words.append(x)
    if x.endswith(("!", "?", ".")):
        end_words.append(x)
    if x.endswith('"'):
        if x[:-1].endswith(("!", "?", ".")):
            end_words.append(x)

for i in range(5):
    word_print = random.choice(start_words)
    stop = False
    while not stop:
        print(word_print, end=" ")
        if word_print in end_words:
            stop = True
            break
        else:
            word_print = random.choice(d[word_print])
    print("\n")




