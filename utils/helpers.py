def removeBlankSpace(string: str) -> str:
    return string.replace(" ", "")

def parseInteger(string: str) -> int:
    return int(string.replace(':', ''))

def matchHoursBetweenPairs(begin_one: int, end_one: int, begin_two: int, end_two: int) -> bool:
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
                begin_peer_one = parseInteger(index_one['begin'])
                end_peer_one   = parseInteger(index_one['end'])
                begin_peer_two = parseInteger(index_two['begin'])
                end_peer_two   = parseInteger(index_two['end'])
                if matchHoursBetweenPairs( begin_peer_one, end_peer_one, begin_peer_two,end_peer_two ):
                    matches+=1                
    return matches