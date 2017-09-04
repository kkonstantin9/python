import sys

words = sys.stdin.readline().split()
uniq_words = []
for word in words:
  uniq_words.append(word.lower())
uniq_words = set(uniq_words)
for word in uniq_words:
  count = 0
  for word_compare in words:
    if word == word_compare.lower():
      count +=1;
  print(word, count, sep=' ')
