from typing import List

VALID_DAYS = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
class Schedule:
    """
        Schedule class
    
        Class to save register of labor day.
    
        Parameters:
        day (str): Days of the week represented by 2 first characters. 'MO' | 'TU' | 'WE' | 'TH' | 'FR' | 'SA' | 'SU'
  
    """
    day: str
    begin: str
    end: str

    def __init__(self, day: str, begin: str, end: str) -> None:
        # Validate day
        if day in  VALID_DAYS:
            self.day = day
        else:
            self.day = None
        # Todo: Validate format of hours
        self.begin = begin
        self.end = end
    
    def saveSchedule(self, arr: List) -> List:
        """
            Method to save Schedule
        
            Parameters:
            arr (List): list to save a list of dictionaries with the format { "day": 'MO, 'begin': '10:00', 'end': '12:00'}
        
            Returns:
            arr (List): A list of dictionaries with the format { "day": 'MO, 'begin': '10:00', 'end': '12:00'} 
        """
        arr.append({ "day": self.day, 'begin': self.begin, 'end': self.end})
        return arr

