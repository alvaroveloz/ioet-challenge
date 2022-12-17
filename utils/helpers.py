def removeBlankSpace(string: str) -> str:
    return string.replace(" ", "")

def parseInteger(string: str) -> int:
    return int(string.replace(':', ''))

def matchHours(begin_one: int, end_one: int, begin_two: int, end_two: int) -> bool:
    if begin_one <= begin_two and end_one >= begin_two:
        return True
    elif begin_one >= begin_two and begin_one <= end_two:
        return True
    elif begin_one >= begin_two and end_one <= end_two:
        return True
    else:
        return False