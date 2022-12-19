from typing import List
from utils.helpers import coincidingOffice
from datetime import datetime

class Output():
    def outputCoincidedInTheOfficeList(registers: List):
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
        return pairs
    
    def outputCoincidedInTheOfficeFile(registers: List):
        now = datetime.now()
        fileName = './data/output/{}_{}.txt'.format(now.strftime('%Y%m%d'), now.strftime('%H%M%S') )       
        file = open(fileName, "w")
        for item in registers:
            data = '{}:{}\n'.format(str(item['pair']), str(item['match']))
            file.write(data)
        
        file.close()
