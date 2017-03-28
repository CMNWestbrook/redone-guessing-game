import random

ran_num = random.randint(1, 100)
# print 'show random int:', ran_num

#greet player
print 'Hello Sweetie!'
#get player name
name = raw_input('What\'s your name? ')
print 'Howdy', name, '!'

print 'The game is to try to guess a random number between 1-100.'
#choose random int between 1-100


def guess():
    num_guesses = 0
    while True:
        try:
            guess = int(raw_input('What\'s your guess? '))
        except ValueError:
            print("Ooppsie! Are you sure that was a number?")
            continue

        if guess > 100 or guess < 1:
            print "Between 1 and 100 silly, you\'re out of range"

        elif guess < ran_num:
            num_guesses += 1
            print "That number is too low."
        elif guess > ran_num:
            num_guesses += 1
            print "That number is too high."
        else:
            print "Congrats, you got it in", num_guesses, "tries!"


guess()
