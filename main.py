from classes.DataReader import FileSource
from classes.Register import Register
from classes.Output import Output

# To get data from file directory /data/input/data.txt
Lines = FileSource().getDataSource()

# To build a List with a new dictionary
registers = Register.buildRegisters(Lines)

# To get pairs and save in a dictionary who coincided in the office
pairs = Output.outputCoincidedInTheOfficeList(registers)

# To send data to output file
Output.outputCoincidedInTheOfficeFile(pairs)

print(pairs)
