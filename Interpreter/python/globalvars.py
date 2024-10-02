word: str = ""
IgnoreSpaces: bool = False
Version: int = 0

def change(valueToChange: str, value):
    global word, IgnoreSpaces, Version

    if valueToChange == 'word':
        word = value
    elif valueToChange == 'IgnoreSpaces':
        IgnoreSpaces = value
    elif valueToChange == 'Version':
        Version = value
    else:
        print(f"No variable named '{valueToChange}'")

