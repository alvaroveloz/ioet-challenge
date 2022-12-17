from typing import List
from classes.Schedule import Schedule
from classes.User import User

class Register:
    user_register: User
    schedule: List[Schedule]

    def __init__(self, user_register: User, schedule: List[Schedule]) -> None:
        self.user_register = user_register
        self.schedule = schedule

    def getPairs():
        pass

    def addRegister(self, arr):
        arr.append({ "user_register": self.user_register, "schedule": self.schedule })
        return arr
