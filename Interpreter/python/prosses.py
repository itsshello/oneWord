from typing import List, Union

import globalvars as gv
from globalvars import SError

def SetWord(word) -> str:
    SError(f"\n1.  | \n     /\\ expected a word to set as a main word").raise_(
    ) and gv.change('Error', True) if word == "" else ...

    gv.change('word', word)
    return word

start: List[Union[str|int]] = []

varrs_: dict[int, List[Union[str|int]]] = {}

def check_start(word_count: int, line_num: int):
    global start
    
    if len(start) == 0:
        if word_count == 3:
            start.append(line_num)

    if len(start) >= 1:
        if start[0] == line_num - 1:
            if word_count == 41:           # 41 type int
                start.append("int")

        if line_num - 2 == start[0]:
            if start[1] == "int":
                start.append(word_count)       # used to add the int var to the list

        if len(start) >= 3:
            if start[1] and start[2] and not len(start) == 4 and line_num - 3 == start[0]:
                if word_count >= 60 and start[1] == 'int':
                    start.append(word_count)

                    varrs_[word_count] = [start[1], start[2]]
                    start = []

                else:
                    SError(f'\n At line {line_num}, expected variable above \n {gv.word + " " * 60} \n [60+] or higher'
                    ).raise_() and gv.change('Error', True)


out: List[Union[str|int]] = []
def check_out(word_count: int, line_num: int):
    global out
    
    if len(out) == 0:
        if word_count == 4:
            out.append(line_num)
    if len(out) == 1:
        if out[0] == line_num - 1:
            print(f"{varrs_[word_count][0]}, {varrs_[word_count][1]}")
            out = []





def prosses_line(word_count: int, line_num: int) -> None:
    gv.change('LineNum', line_num)
    """Line 2 to 3"""
    if line_num <= 3:
        gv.change('IgnoreSpaces', True if word_count == 2 else False) if line_num == 2 and word_count > 1 else SError(f"\
            \n1.  | . . . \n2.  | \n    /\\ expected {gv.word} {gv.word} or {gv.word} {gv.word} {gv.word} at Line 2 \n\
                This line is used to set to turn on or turn off IgnoreSpaces").raise_() and gv.change('Error', True
            ) if line_num == 2 else ...

        gv.change('Version', word_count) if line_num == 3 else ...
        return

    """___main___"""
    check_start(word_count, line_num)
    check_out(word_count, line_num)



    

    
    
    