class Schedule:
    day: str
    begin: str
    end: str

    def __init__(self, day: str, begin: str, end: str) -> None:
        self.day = day
        self.begin = begin
        self.end = end

