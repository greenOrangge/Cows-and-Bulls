from random import randint

# Random word list
word_list = ['CHAI', 'CHAL', 'CHAM', 'CHAO', 'CHAP']

# finding the length of the word list for random function
length = len(word_list) - 1

# initialising cow and bull
cow, bull = 0, 0

# word the user will guess
word_to_guess = list(word_list[randint(0, length)])
# print(word_to_guess)
word_to_guess_pos = list()

for i in word_to_guess:
    place = word_to_guess.index(i)
    word_to_guess_pos.append(place)
# print(word_to_guess_pos)

while True:
    #user's input for guessing the word
    guess = list(input("Enter your first guess:").upper())

    for letter in guess:
        if letter in word_to_guess:
            pos = guess.index(letter)
            actual_place = word_to_guess.index(letter)
            if pos == actual_place:
                # print("BULL")
                bull += 1
            elif pos != actual_place:
                # print("COW")
                cow += 1
            
    print("Cow = " + str(cow) + " Bull = " + str(bull))
    
    if bull == 4:
        print("Congrats! You have found the word:\n" + ''.join(word_to_guess))
        quit()
    cow, bull = 0, 0