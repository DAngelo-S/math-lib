class MatrixsWithDifferentDimensionsException(Exception):
    def __init__(self):
        super().__init__("Matrixs with different dimensions")

class NotANumberException(Exception):
    def __init__(self):
        super().__init__("Not a number.")

class InvalidDimensionsForMultiplyingColumnsException(Exception):
    def __init__(self):
        super().__init__("Invalid dimensions for multiplying columns")

class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__("Invalid type")