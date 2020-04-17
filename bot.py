import pickle
import os.path
import sys

answers = ['Dykstra', 'Backman', 'Hernandez', 'Carter', 'Strawberry', 'Foster', 'Johnson', 'Santana', 'Gooden']

if (os.path.exists('bot_state.p')):
    (answered_by, incorrect_guesses) = pickle.load(open("bot_state.p", "rb"))
else:
    answered_by = {}
    for answer in answers:
        answered_by[answer] = None

    incorrect_guesses = []

guesses = sys.argv[2:]
guesser = sys.argv[1]
print(f'{guesser}\'s Guesses:')
for guess in guesses:
    if guess in answers:
        if answered_by[guess]:
            print(f"{guess}: Correct, but already named by {answered_by[guess]}")
        else:
            print(f"{guess}: DING!  Correct")
            answered_by[guess] = guesser
    else:
        print(f"{guess}: Incorrect")
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)


print()
print('Correct Answers:')
for (answer, named_by) in answered_by.items():
    print(f"{answer} ({named_by})" if named_by else "UNNAMED")

print()
print('Incorrect guesses:')
for guess in incorrect_guesses:
    print(guess)

pickle.dump((answered_by, incorrect_guesses), open("bot_state.p", "wb"))
