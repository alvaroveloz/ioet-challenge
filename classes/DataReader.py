from abc import ABC, abstractmethod

class DataReader(ABC):
    @abstractmethod
    def getDataSource():
        pass

class FileSource(DataReader):
    @staticmethod
    def getDataSource():
        file = open('./data/input/2022-12-W1.txt', 'r')
        return file.readlines()

class MemorySource(DataReader):
    @staticmethod
    def getDataSource():
        pass
        