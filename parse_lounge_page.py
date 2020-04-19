from bs4 import BeautifulSoup


def get_lounge_posts(fp):
    soup = BeautifulSoup(fp, features="lxml")
    for post in soup('div', 'post'):
        yield post


with open("fixtures/lounge_6329_600.html") as fp:
    for post in get_lounge_posts(fp):
        username = post.parent.parent.a.text
        post_time = post.parent.parent.parent.find_all('td')[1].text[8:]

        if '#LoungeTrivia_86Mets' not in post.text or 'Harold' in username:
            continue

        # The guesses are in the text that follows the quote
        # So find the quote, and then move to the following siblings
        cursor = post.blockquote
        guesses = []
        while cursor and cursor.find_next_sibling('p'):
            cursor = cursor.find_next_sibling('p')
            guesses += cursor.text.split("\n")  # guesses may be in multiple lines in one <p>

        print(f"{post_time} {username}: {guesses}")
