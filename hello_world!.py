f = open("persian_stop_words.txt")
words = []
for i in f:
    words.append(f.readline())
print(words)
