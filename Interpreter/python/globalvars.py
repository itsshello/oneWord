word: str = ""
IgnoreSpaces: bool = False
Version: int = 0
Error: bool = False
LineNum: int = 0

class sErrorHelper(Exception):
    ...

class SError:
    global LineNum
    
    def __init__(self, txt):
        self.txt = txt
    
    def raise_(self):
        raise sErrorHelper(self.txt + 'from Line :' + LineNum)

def change(valueToChange: str, value):
    global word
    global IgnoreSpaces
    global Version
    global Error
    global LineNum

    if valueToChange == 'word':
        word = value
    elif valueToChange == 'IgnoreSpaces':
        IgnoreSpaces = value
    elif valueToChange == 'Version':
        Version = value
    elif valueToChange == 'Error':
        Error = value
    elif valueToChange == 'LineNum':
        LineNum = value
    else:
        print(f"No variable named '{valueToChange}'")

