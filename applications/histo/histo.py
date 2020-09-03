with open("robin.txt") as f:
    words = f.read()

def word_count(s):
    # Your code here

    punctuation = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    for x in punctuation:
        s = s.replace(x, '')

    words = s.split()

    dict = {}

    for word in words:
        if word.lower() in dict:
            dict[word.lower()] += 1
        else:
            dict[word.lower()] = 1

    return dict

word_dict = word_count(words)
max_space = max(len(x) for x in word_dict)

sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse = True)


for x in sorted_dict:
    print(x[0], " " * (max_space - len(x[0])), "#" * x[1])

