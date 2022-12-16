
def removeBlankSpace(string):
    return string.replace(" ", "")

# Using readlines()
file1 = open('../data/2022-12-W1.txt', 'r')
Lines = file1.readlines()
 
count = 0
registers= []
# Strips the newline character
for line in Lines:
    count += 1
    dict_user_register = {}    
    raw_register = line.strip().split('=')
    user = raw_register[0]
    dict_user_register['user_register'] = user
    raw_schedule = raw_register[1].split(',')
    schedule = []
    print(raw_register)
    # Get days
    for day_register in raw_schedule:
        
        day_register = removeBlankSpace(day_register)
        day, begin, end = day_register[0:2], day_register[2:7], day_register[8:]
        schedule.append({ "day": day, 'begin': begin, 'end': end})
        #print(day, begin, end)
    dict_user_register['schedule'] = schedule
    registers.append(dict_user_register)
        
#registers contains data in an array of dictionaries
for register in registers:
    print(register)

