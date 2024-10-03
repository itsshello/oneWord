word: str = ""
IgnoreSpaces: bool = False
Version: int = 0
Error: bool = False

class sErrorHelper(Exception):
    ...

class SError:
    def __init__(self, txt):
        self.txt = txt
    
    def raise_(self):
        raise sErrorHelper(self.txt)

def change(valueToChange: str, value):
    global word
    global IgnoreSpaces
    global Version
    global Error

    if valueToChange == 'word':
        word = value
    elif valueToChange == 'IgnoreSpaces':
        IgnoreSpaces = value
    elif valueToChange == 'Version':
        Version = value
    elif valueToChange == 'Error':
        Error = value
    else:
        print(f"No variable named '{valueToChange}'")

