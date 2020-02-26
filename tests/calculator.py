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