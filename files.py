from classes.Register import Register
from classes.User import User
from classes.Schedule import Schedule
from utils.helpers import removeBlankSpace, parseInteger, matchHours


def coincidingOffice(peer_one: object, peer_two: object) -> int: 
    matches = 0   
    for index_one in peer_one:
        for index_two in peer_two:
            if index_one['day'] == index_two['day']:
                print('{} its equal to {}'.format(index_one, index_two))       
                # hours validation intersection 
                begin_peer_one = parseInteger(index_one['begin'])
                end_peer_one   = parseInteger(index_one['end'])
                begin_peer_two = parseInteger(index_two['begin'])
                end_peer_two   = parseInteger(index_two['end'])
                if matchHours( begin_peer_one, end_peer_one, begin_peer_two,end_peer_two ):
                    matches+=1
                
    return matches

# Using readlines()
file1 = open('./data/2022-12-W1.txt', 'r')
Lines = file1.readlines()
 

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
    registers = register.addRegister(registers)


# Creating pairs and validating matches
pairs = []
maximum_pairs = len(registers)-1

# Getting the dict to send in output
for index, peer_one in enumerate(registers, 0):
    index_peer = index
    match = 0
    for peer_two in enumerate(registers, 0):
        # Getting peers to compare
        
        if index_peer < maximum_pairs:
            pair = '{}-{}'.format(registers[index]['user_register'], registers[index_peer+1]['user_register'])
            # to search matches
            match = coincidingOffice( registers[index]['schedule'], registers[index_peer+1]['schedule'] )
            pairs.append({ 'pair': pair, 'match':match})
            index_peer+=1

print(pairs)
#print function to output data with pairs created

