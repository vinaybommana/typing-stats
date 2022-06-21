from bs4 import BeautifulSoup
import re

# GUTENBURG_LINK = "https://www.gutenberg.org/files/2852/2852-h/2852-h.htm"
NOVEL_FILE_NAME = "hound-of-baskerville.html"


def get_file_contents(NOVEL_FILE_NAME):
    with open(NOVEL_FILE_NAME) as h:
        file_contents = h.read()
    return str(file_contents)


def clean_file_content(file_contents):
    # replace &ldquo; to "
    # replace &rdquo; to "
    if type(file_contents) == "str":
        file_contents = file_contents.replace("&ldquo;", '"')
        file_contents = file_contents.replace("&rdquo;", '"')
    return file_contents


def parse_html(file_contents):
    soup = BeautifulSoup(file_contents, 'html.parser')
    text = soup.get_text()
    paragraphs = text.split("\n\n")
    paragraphs = [item.replace("\n", "") for item in paragraphs]
    paragraphs = [item for item in paragraphs if item]
    with open("hound-of-baskerville.txt", "w+") as h:
        for para in paragraphs:
            para = para.strip()
            para = re.sub(' {2,}', ' ', para)
            para = para.replace("“", '"')
            para = para.replace("”", '"')
            para = para.replace("’", "'")
            para = para.replace("‘", "'")
            h.write(para)
            h.write("\n")

def main():
    file_contents = get_file_contents(NOVEL_FILE_NAME)
    parse_html(file_contents)


if __name__ == "__main__":
    main()
