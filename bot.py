import parse_lounge_page as parser

correct_answers = ['Dykstra', 'Backman', 'Hernandez', 'Carter',
                   'Strawberry', 'Foster', 'Johnson', 'Santana', 'Gooden']

already_answered = {}
incorrect_guesses = []


def print_header(header):
    print()
    print(header)


def print_row(row):
    print(f"  {row}")


def sanitize_guess(guess):
    return guess.strip()


def get_guesses():
    with open("fixtures/lounge_6329_600_mod.html") as fp:
        for response in parser.get_guesses(fp):
            yield response


for response in get_guesses():
    guesser = response['username']
    guesses = map(sanitize_guess, response['guesses'])
    print_header(f'{guesser}\'s Guesses (post {response["num"]}):')
    for guess in guesses:
        if guess in already_answered:
            print_row(f"{guess}: Correct, but already named by " +
                      f"{already_answered[guess]['username']}")
        elif guess in correct_answers:
            print_row(f"{guess}: DING!  Correct")
            already_answered[guess] = response
        else:
            print_row(f"{guess}: Incorrect")
            if guess not in incorrect_guesses:
                incorrect_guesses.append(guess)


print_header('Correct answers:')
for answer in correct_answers:
    if answer in already_answered:
        print_row(f"{answer} ({already_answered[answer]['username']})")
    else:
        print_row("UNNAMED")

print_header('Incorrect guesses:')
for guess in incorrect_guesses:
    print_row(guess)
