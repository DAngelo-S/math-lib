class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__("Invalid type.")
    
class DivergeColumnsSizeException(Exception):
    def __init__(self):
        super().__init__("Different columns sizes")

class InvalidPivot(Exception):
    def __init__(self):
        super().__init__("Zero pivot found. Pivoting not implemented.")