import globalvars as gv

def prosses_line(word_count: int, line_num: int, lineContent: str = "") -> None:
    gv.change('word', lineContent) if line_num == 1 else ...
    gv.change('IgnoreSpaces', True if word_count == 2 else False) if line_num == 2 else ...
    gv.change('Version', word_count) if line_num == 3 else ...

    

    
    
    