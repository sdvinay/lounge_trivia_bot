import csv

answers = ['Dykstra', 'Backman', 'Hernandez', 'Carter', 'Strawberry', 'Foster', 'Johnson', 'Santana', 'Gooden']

answered_by = {}
for answer in answers:
    answered_by[answer] = None

incorrect_guesses = []

with open('fixtures/guesses.csv') as f:
    reader = csv.reader(f)
    for response in reader:
        guesser = response[0]
        guesses = response[1:]
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
