'''Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и
age. По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять
методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName
нужен для получения данных об имени конкретного студента, метод getAge нужен для
получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для
получения данных о номере группы конкретного студента. Метод SetNameAge позволяет
изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет
изменить номер группы установленный по умолчанию. В программе необходимо создать пять
экземпляров класса Student, установить им разные имена, возраст и номер группы.
'''


# создаем класс Student
class Student:
    def __init__(self, name="Ivan", groupNumber = "10A", age = 18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    # метод getName-для получения данных об имени конкретного студента
    def getName(self):
        print ("Имя студента:", self.name)

    # метод getAge- для получения данных о возрасте конкретного студента
    def getAge(self):
        print ("Возраст студента:", self.age)

    # метод getGroupNumber-для получения данных о номере группы конкретного студента
    def getGroupNumber(self):
        print ("Номер группы:", self.groupNumber)
    
    # метод setNameAge-изменить данные атрибутов установленных по умолчанию
    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    # метод setGroupNumber-позволяет изменить номер группы установленный по умолчанию
    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

# Объекты класса Student
Dmitry = Student("Dmitry", 30, "10B")
Anna = Student("Anna", 29, "11C")
Viktor = Student("Viktor", 28, "12D")
Mikhail = Student("Mikhail", 39, "13F")
Andrey = Student("Andrey", 40, "14G")
         

      


   



