import datetime
from time import time

def removeBlankSpace(string: str) -> str:
    return string.replace(" ", "")

def matchHoursBetweenPairs(begin_one: time, end_one: time, begin_two: time, end_two: time) -> bool:
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
                # print('{} its equal to {}'.format(index_one, index_two))       
                # hours validation intersection 
                begin_peer_one = datetime.time.fromisoformat(index_one['begin'])
                end_peer_one   = datetime.time.fromisoformat(index_one['end'])
                begin_peer_two = datetime.time.fromisoformat(index_two['begin'])
                end_peer_two   = datetime.time.fromisoformat(index_two['end'])
                if matchHoursBetweenPairs( begin_peer_one, end_peer_one, begin_peer_two,end_peer_two ):
                    matches+=1                
    return matches