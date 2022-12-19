from typing import List
from classes.Schedule import Schedule
from classes.User import User
from utils.helpers import removeBlankSpace

class Register:
    user_register: User
    schedule: List[Schedule]

    def __init__(self, user_register: User, schedule: List[Schedule]) -> None:
        self.user_register = user_register
        self.schedule = schedule

    def getPairs():
        pass

    def addRegisterToList(self, arr: List):
        arr.append({ "user_register": self.user_register, "schedule": self.schedule })
        return arr

    def buildRegisters(Lines: str):        
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
