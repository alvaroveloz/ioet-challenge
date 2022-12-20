from abc import ABC, abstractmethod
import os

# Todo: to handle .env variables with python-dotenv 
FILE_SOURCE_DATA_DIRECTORY = '/data/input/'

class DataReader(ABC):
    """Abstract class to extend diferents sources of data"""
    @abstractmethod
    def getDataSource():
        pass

class FileSource(DataReader):
    @staticmethod
    def getDataSource()->list[str]:
        """ 
            Method that read the file with the name that user type in console
            
            Returns:
            list[str]: A list of raw strings from file   
        """
        pathlib = os.path.abspath(os.getcwd()) + FILE_SOURCE_DATA_DIRECTORY
        user_input = input('Enter the name of the file to export content:')
        user_enter_extension = user_input[-4:].__contains__('.txt')
        
        try:
            # Validating if user enter the extension
            if user_enter_extension:
                fullpath = '{}{}'.format(pathlib, user_input)
            else: 
                fullpath = '{}{}{}'.format(pathlib, user_input,'.txt')
            
            file = open(fullpath, 'r')
        except FileNotFoundError:
            print("File not found. Check the path variable and filename")
            exit()
        else:
            return file.readlines()

class MemorySource(DataReader):
    @staticmethod
    def getDataSource():
        pass
        