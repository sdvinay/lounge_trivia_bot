from bs4 import BeautifulSoup


class LoungePost:
    """ A lounge post"""


def get_lounge_posts(fp):
    soup = BeautifulSoup(fp, features="lxml")
    for post in soup('div', 'post'):  # <div class="post">
        response = LoungePost()
        response.text = post.text
        response.soup = post.parent.parent.parent
        response.username = post.parent.parent.a.text
        if 'Harold' in response.username:
            continue
        response.time = response.soup.find_all('td')[1].text[8:]
        response.num = response.soup.find_all('a')[3].text[2:]
        response.id = response.soup.find_all('a')[3]['name']
        yield response


def get_guesses(fp):
    for response in get_lounge_posts(fp):

        if '#LoungeTrivia_86Mets' not in response.text:
            continue

        # The guesses are in the text that follows the quote
        # So find the quote, and then move to the following siblings
        cursor = response.soup.blockquote
        response.guesses = []
        # guesses might be in separate <p>s or in separate lines in one <p>
        while cursor and cursor.find_next_sibling('p'):
            cursor = cursor.find_next_sibling('p')
            response.guesses += cursor.text.split("\n")

        yield(response)


if __name__ == "__main__":
    with open("fixtures/lounge_6329_600.html") as fp:
        for response in get_guesses(fp):
            print(response)
