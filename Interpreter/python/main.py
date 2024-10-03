import re
from prosses import *
from globalvars import *

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

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            line_num: int = 0  # 1 because the 1st line will be checked not in the loop 
            Text = file.read()
            Lines = Text.split('\n')
            word = SetWord(Lines[0])

            for line in Lines:
                line_num += 1
                if line_num == 1:
                    continue
                words = words_inSentence(line, word)
                prosses_line(words, line_num) if line_num == 1 else prosses_line(words, line_num)
                if Error:
                    break

    except FileNotFoundError as e:
        print("File Not Found")

if __name__ == "__main__":
    read_file('./../../main.ow')