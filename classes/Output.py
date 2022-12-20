from typing import List
from utils.helpers import coincidingOffice
from datetime import datetime

class Output():
    """
        Output Class to get all the coincidences and return data in file or console.
  
        Parameters:
            registers (Register): A List of Registers class to verify coincidences
        Returns:
            arr (List): A list of coincidences between two users.
    """
    registers: List

    def __init__(self, registers) -> None:
        self.registers = registers

    def outputCoincidedInTheOfficeList(self):
        # Creating pairs and validating matches
        pairs = []
        maximum_pairs = len(self.registers)-1

        # Getting the dict to send in output
        for index, peer_one in enumerate(self.registers, 0):
            index_peer = index
            match = 0
            for peer_two in enumerate(self.registers, 0):
                # Getting peers to compare
                
                if index_peer < maximum_pairs:
                    pair = '{}-{}'.format(self.registers[index]['user_register'], self.registers[index_peer+1]['user_register'])
                    # to search matches
                    match = coincidingOffice( self.registers[index]['schedule'], self.registers[index_peer+1]['schedule'] )
                    pairs.append({ 'pair': pair, 'match':match})
                    index_peer+=1
        return pairs
    
    def outputCoincidedInTheOfficeFile(registers: List):
        """
            Output Class Method to generate a file with coincidences in the office in /data/output/ directory.
    
            Parameters:
                registers (Register): A List of Registers class to verify coincidences        
        """
        now = datetime.now()
        fileName = './data/output/{}_{}.txt'.format(now.strftime('%Y%m%d'), now.strftime('%H%M%S') )       
        file = open(fileName, "w")
        for item in registers:
            data = '{}:{}\n'.format(str(item['pair']), str(item['match']))
            file.write(data)
        file.close()

    def outputCoincidedInTheOfficeTable(registers: List):
        """
            Output Class Method to show a table coincidences in the office through console.
    
            Parameters:
                registers (Register): A List of Registers class to verify coincidences        
        """
        now = datetime.now()
        for item in registers:
            data = '{}:\t{}\n'.format(str(item['pair']), str(item['match']))
            print(data)
