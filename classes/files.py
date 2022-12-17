
def removeBlankSpace(string):
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
file1 = open('../data/2022-12-W1.txt', 'r')
Lines = file1.readlines()
 

registers= []
# Strips the newline character
for line in Lines:
    dict_user_register = {}    
    raw_register = line.strip().split('=')
    user = raw_register[0]
    dict_user_register['user_register'] = user
    raw_schedule = raw_register[1].split(',')
    schedule = []
    
    # Get days
    for day_register in raw_schedule:
        
        day_register = removeBlankSpace(day_register)
        day, begin, end = day_register[0:2], day_register[2:7], day_register[8:]
        schedule.append({ "day": day, 'begin': begin, 'end': end})
        #print(day, begin, end)
    dict_user_register['schedule'] = schedule
    registers.append(dict_user_register)
        
#registers contains data in an array of dictionaries

pairs = []
maximum_pairs = len(registers)-1

for index, peer_one in enumerate(registers, 0):
    index_peer = index
    match = 0
    for peer_two in enumerate(registers, 0):
        # Getting peers to compare
        
        if index_peer < maximum_pairs:
            pair = '{}-{}'.format(registers[index]['user_register'], registers[index_peer+1]['user_register'])
            print('{}-{}'.format(registers[index]['user_register'], registers[index_peer+1]['user_register'] ))
            match = coincidingOffice( registers[index]['schedule'], registers[index_peer+1]['schedule'] )                
            pairs.append({ 'pair': pair, 'match':match})
            
            index_peer+=1

print(pairs)
#print function to output data with pairs created

