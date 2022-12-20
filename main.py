from classes.DataReader import FileSource
from classes.Register import Register
from classes.Output import Output

def main():

    # To get data from file directory
    Lines = FileSource().getDataSource()

    # To build a List with a new dictionary
    registers = Register.buildRegisters(Lines)

    # To get pairs and save in a dictionary who coincided in the office
    output = Output(registers)
    pairs = output.outputCoincidedInTheOfficeList()

    # To send data to output file
    #Output.outputCoincidedInTheOfficeFile(pairs)

    # To show data as a table
    Output.outputCoincidedInTheOfficeTable(pairs)

if __name__ == "__main__":
    main()