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
            line_num: int = 0
            code_line_num: int = 0
            Text = file.read()
            Lines = Text.split('\n')
            word = SetWord(Lines[0])

            for line in Lines:
                line_num += 1
                change('LineNum', line_num)

                words = words_inSentence(line, word)
                if words == 0 or words == "":
                    continue

                code_line_num += 1
                if code_line_num == 1:
                    continue
                    
                prosses_line(words, code_line_num)
                if Error:
                    break
                # print(words)

    except FileNotFoundError as e:
        print("File Not Found")

if __name__ == "__main__":
    read_file('./../../main.ow')