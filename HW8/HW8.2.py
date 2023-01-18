"""Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы
addition — сложение, multiplication — умножение, division — деление, subtraction —
вычитание. При передаче в методы параметров a и b с ними нужно производить
соответствующие действия и печатать ответ.
"""
#создаем класс Math
class Math:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    #метод addition
    def addition(self):
        print(self.a+self.b)

    #метод multiplication
    def multiplication(self):
        print(self.a*self.b)

    #метод division
    def division(self):
        print(self.a/self.b)

    #метод subtraction
    def subtraction(self):
        print(self.a-self.b)




