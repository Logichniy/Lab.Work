from collections import Counter
words = open("In Winter I get up at night.txt").read().lower().split()
counter = Counter(words)
print(counter)
print(counter.most_common(1))
word = counter.most_common(1)[0][0]
print(word)