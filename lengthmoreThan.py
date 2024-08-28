S = input("Enter the sentence: ")
n = int(input("Enter the length: "))
words = S.split()
long_words = [word for word in words if len(word) >= n]
print(f"Words longer than {n} characters: {long_words}")
