from typing import Any, Union

word: str = ""
IgnoreSpaces: bool = False
Version: int = 0
Error: bool = False
LineNum: int = 0
DevMode: bool = True

Types: dict[str, int] = {
    "int": 41,
    "Unicode": 42,
    "ASCII": 43
}
Prosses: dict[str, int] = {
    "Start": 3,
    "Output": 4,
    "Input": 5
}

class sErrorHelper(Exception):
    ...

class SError:
    global LineNum

    def __init__(self, txt):
        self.txt = txt
    
    def raise_(self):
        raise sErrorHelper("\n\n" + self.txt + '\nfrom Line : ' + str(LineNum))

def removeType(var) -> Any:
    return var

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

