class Calculator:
    answer = 0 

    def __init__(self):
        pass

    @classmethod
    def add(cls, num):
        cls.answer += num
        return cls.answer

    @classmethod
    def subtract(cls, num):
        cls.answer -= num
        return cls.answer
    
    classmethod
    def multiply(cls, num):
        cls.answer *= num
        return cls.answer
    
    @classmethod
    def divide(cls, num):
        cls.answer /= num
        return cls.answer
    
    @classmethod
    def square(cls, num):
        cls.answer = num**2
        return cls.answer

    @classmethod
    def squareRoot(cls, num):
        cls.answer = num**.5
        return cls.answer
        
    @classmethod
    def getAnswer(cls):
        return cls.answer

    