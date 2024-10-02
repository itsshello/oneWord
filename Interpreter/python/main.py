import re

word: str = "azz"
IgnoreSpaces: bool = False

def words_inSentence(text, word) -> int :
    global IgnoreSpaces
    textt = re.compile(re.escape(word), re.IGNORECASE)

    if IgnoreSpaces:
        clean = re.sub(r'\s+', '', text)
        matchs = re.findall(textt, clean)

        return len(matchs)
    else:
        splits = text.split(word)

        return len(splits) - 1

def read_file(filename, word):
    try:
        with open(filename, 'r') as file:
            Text = file.read()
            Lines = Text.split('\n')
            for line in Lines:
                print(line)
                words = words_inSentence(line, word)
                print(words)

    except FileNotFoundError as e:
        print("File Not Found")

if __name__ == "__main__":
    read_file('./../../main.ow', word)