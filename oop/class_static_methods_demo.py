class Calculator:
    calculation_type = Arithmetic Operations
    def __init__(self, add):
        self.add = add
        
    @staticmethod
    def add(a, b):
        return a + b

    def __init__(self, multiply):
        self.multiply = multiply
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


