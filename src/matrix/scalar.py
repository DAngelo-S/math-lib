from .error import NotANumberException, InvalidTypeException

class Scalar():
    def __init__(self, v):
        if not isinstance(v, int) and not isinstance(v, float):
            raise NotANumberException()

        self.value = v
    
    def __mul__(self, other):
        from .matrix import Matrix
        if isinstance(other, Matrix):
            return other * self
        
        elif isinstance(other, Scalar):
            return Scalar(self.value * other.value)
        
        else:
            raise InvalidTypeException()
        
    def __add__(self, other):
        return Scalar(self.value + other.value)

    def __sub__(self, other):
        return Scalar(self.value - other.value)