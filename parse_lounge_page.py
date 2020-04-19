import csv
from bs4 import BeautifulSoup


def get_lounge_posts(fp):
    soup = BeautifulSoup(fp, features="lxml")
    for post in soup('div', 'post'):  # <div class="post">
        yield post


def get_guesses(fp):
    for post in get_lounge_posts(fp):
        username = post.parent.parent.a.text

        if '#LoungeTrivia_86Mets' not in post.text or 'Harold' in username:
            continue

        response = {}
        response['username'] = username
        response['time'] = post.parent.parent.parent.find_all('td')[1].text[8:]
        response['num'] = post.parent.parent.parent.find_all('a')[3].text[2:]
        response['id'] = post.parent.parent.parent.find_all('a')[3]['name']

        # The guesses are in the text that follows the quote
        # So find the quote, and then move to the following siblings
        cursor = post.blockquote
        response['guesses'] = []
        # guesses might be in separate <p>s or in separate lines in one <p>
        while cursor and cursor.find_next_sibling('p'):
            cursor = cursor.find_next_sibling('p')
            response['guesses'] += cursor.text.split("\n")

        yield(response)


if __name__ == "__main__":
    with open("fixtures/lounge_6329_600.html") as fp:
        with open('guesses_6329_600.csv', 'w', newline='') as csvfile:
            fieldnames = ['time', 'num', 'id', 'username', 'guesses']
            writer = csv.DictWriter(csvfile, fieldnames)
            for response in get_guesses(fp):
                print(response)
                writer.writerow(response)
