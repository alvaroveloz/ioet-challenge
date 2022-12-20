class User:
    """
        User class to handle users.
    
        Parameters:
        name (str): Name of the user  
    """
    name: str

    def __init__(self, name: str) -> None:
        self.name = name
        
