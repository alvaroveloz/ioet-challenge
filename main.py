from classes.DataReader import FileSource
from classes.Register import Register
from classes.Output import Output

Lines = FileSource().getDataSource()
registers = Register.buildRegisters(Lines)
pairs = Output.outputCoincidedInTheOfficeList(registers)
Output.outputCoincidedInTheOfficeFile(pairs)

print(pairs)
