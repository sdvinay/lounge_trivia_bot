import csv

answers = ['Dykstra', 'Backman', 'Hernandez', 'Carter', 'Strawberry', 'Foster', 'Johnson', 'Santana', 'Gooden']

answered_by = {}
for answer in answers:
    answered_by[answer] = None

incorrect_guesses = []


def print_header(header):
    print()
    print(header)


def print_row(row):
    print(f"  {row}")


with open('fixtures/guesses.csv') as f:
    reader = csv.reader(f)
    for response in reader:
        guesser = response[0]
        guesses = response[1:]
        print_header(f'{guesser}\'s Guesses:')
        for guess in guesses:
            if guess in answers:
                if answered_by[guess]:
                    print_row(f"{guess}: Correct, but already named by {answered_by[guess]}")
                else:
                    print_row(f"{guess}: DING!  Correct")
                    answered_by[guess] = guesser
            else:
                print_row(f"{guess}: Incorrect")
                if guess not in incorrect_guesses:
                    incorrect_guesses.append(guess)


print_header('Correct Answers:')
for (answer, named_by) in answered_by.items():
    print_row(f"{answer} ({named_by})" if named_by else "UNNAMED")

print_header('Incorrect guesses:')
for guess in incorrect_guesses:
    print_row(guess)
