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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))