class MatricesWithDifferentDimensionsException(Exception):
    def __init__(self):
        super().__init__("Matrices with different dimensions")

class NotANumberException(Exception):
    def __init__(self):
        super().__init__("Not a number.")

class InvalidDimensionsForMultiplyingColumns(Exception):
    def __init__(self):
        super().__init__("Invalid dimensions for multiplying columns")

class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__("Invalid type")