from typing import List
from classes.Schedule import Schedule
from classes.User import User
from utils.helpers import removeBlankSpace

class Register:
    """
        Register Class to save register of users and lists of schedules.
  
        Parameters:
            user_register (User): instance of User class
            schedule (List[Schedule]): instance of Lists of Schedule.
    """
    user_register: User
    schedule: List[Schedule]

    def __init__(self, user_register: User, schedule: List[Schedule]) -> None:
        self.user_register = user_register
        self.schedule = schedule

    def addRegisterToList(self, arr: List)->List:
        """
            Method to save objects in list of Register instance.
    
            Parameters:
                arr (Register):  list of instances of Register class
                
            Return:
                arr (Register): list of instances of Register class
        """
        arr.append({ "user_register": self.user_register, "schedule": self.schedule })
        return arr

    def buildRegisters(Lines: str)->List:
        """
            Method to get data from files. Return a list of depured objects.
    
            Parameters:
                Lines (str):  A list of raw strings from file.
                
            Return:
                List (Register): A list of instances of Register class
        """
        registers= []
        # Strips the newline character
        for line in Lines:
            raw_register = line.strip().split('=')
            user = User(raw_register[0]) 
            raw_schedule = raw_register[1].split(',')
            arr_schedule = []
            
            # Get days
            for item in raw_schedule:
                item = removeBlankSpace(item)
                schedule = Schedule(item[0:2], item[2:7], item[8:])
                schedule.saveSchedule(arr_schedule)
                
            register  = Register(user.name, arr_schedule) 
            registers = register.addRegisterToList(registers)

        return registers
