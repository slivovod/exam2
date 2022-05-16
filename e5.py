def queue(string):
    words = string.split()
    correct_words_queue = sorted(words, key=find_digit)
    return " ".join(correct_words_queue)

def find_digit(word):
    for i in word:
        if i.isdigit():
            return int(i)
    return None

str = "4of Fo1r pe6ople g3ood th5e the2"
print(queue(str))