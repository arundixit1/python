from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        linewords = line.decode('utf-8')
        print(linewords)
    story.close()
    print(story_words)


