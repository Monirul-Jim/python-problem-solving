sentence = input('Enter a sentence : ')
words = sentence.split()
reversed_word = [word[::-1] for word in words]
result = ' '.join(reversed_word)

print(result)
