# -*- coding: utf-8 -*-
# encoding=utf8

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

    @classmethod
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

if __name__ == "__main__":
    calc = Calculator()
    choice = ''

    print('Select operation!')
    print('1.Add (+)')
    print('2.Subtract (-)')
    print('3.Multiply (*)')
    print('4.Divide (/)')
    print('5.Square (**)')
    print('6.Get square root (√)')
    print('7.Quit')

    choice = input('Enter choice:')
    number = float(input('Enter number:'))

    if choice == "1":
        print(Calculator.answer, "+", number, "=", Calculator.add(number))
    elif choice == "2":
        print(Calculator.answer, "-", number, "=", Calculator.subtract(number))
    elif choice == "3":
        print(Calculator.answer, "*", number, "=", Calculator.multiply(number))
    elif choice == "4":
        print(Calculator.answer, "/", number, "=", Calculator.divide(number))
    elif choice == "5":
        print(Calculator.answer, "**", number, "=", Calculator.square(number))
    elif choice == "6":
        print(Calculator.answer, "√", number, "=", Calculator.squareRoot(number))
    else:
        print("(•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ ) something went wrong (•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ )")