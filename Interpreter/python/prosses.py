import globalvars as gv
from globalvars import SError

def SetWord(word) -> str:
    gv.change('word', word)
    return word


def prosses_line(word_count: int, line_num: int) -> None:
    """Line 2 to 3"""
    gv.change('IgnoreSpaces', True if word_count == 2 else False) if line_num == 2 and word_count > 1 else SError(f"\
        \n1.  | . . . \n2.  | \n    /\\ expected {gv.word} {gv.word} or {gv.word} {gv.word} {gv.word} at Line 2 \n\
            This line is used to set to turn on or turn off IgnoreSpaces").raise_() and gv.change('Error', True)

    gv.change('Version', word_count) if line_num == 3 else ...

    """___main___"""



    

    
    
    