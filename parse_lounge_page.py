from bs4 import BeautifulSoup


def get_lounge_posts(fp):
    soup = BeautifulSoup(fp, features="lxml")
    for post in soup('div', 'post'):
        yield post


with open("fixtures/lounge_6329_600.html") as fp:
    for post in get_lounge_posts(fp):
        if '#LoungeTrivia_86Mets' not in post.text:
            continue

        username = post.parent.parent.a.text
        if 'Harold' in username:
            continue

        post_time = post.parent.parent.parent.find_all('td')[1].text
        cursor = post.blockquote
        guesses = []
        while cursor and cursor.find_next_sibling('p'):
            cursor = cursor.find_next_sibling('p')
            guesses += cursor.text.split("\n")

        print(username, post_time, guesses)
