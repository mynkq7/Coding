# Print numbers
number_list = [1,2,3,4,5,6,7,8,9,10]
for num in number_list:
    print(f"Here is your number {num}")

# Print word numbers
word_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for words in word_list:
    print(f"Here is your number: {words}")

# Skip a single letter
Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in Alphabets:
    if letter =="M":
     print("Removing letter M")
     continue
    print(f'Here is your Alphabet: {letter}')
# Skip multiple letters
Alphabets_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_to_skip = "BFJNQ"

for newwords in Alphabets_2:
    if newwords in letters_to_skip:
        print(f"Removing unwanted letter: {newwords}")
        continue
    print(f"Here is your Letter {newwords}")
