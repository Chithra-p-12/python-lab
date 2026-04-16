word = input("Enter a word: ")
reversed_word = ""
i = len(word) - 1   
while i >= 0:
    reversed_word += word[i]
    i -= 1
print(f"The reverse of '{word}' is '{reversed_word}'")
