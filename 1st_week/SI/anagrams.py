words = []
with open('anagrams.csv', 'r') as file:
    lines = file.readlines()
words = [element.replace("\n", "") for element in lines]

anagram_words = ""
for i in words:
    for j in words:
        if i[::-1] == j:
            if i not in (anagram_words):
                anagram_words += i + (" " * (8 - len(j)))
                anagram_words += j + "\n"
print(anagram_words)
