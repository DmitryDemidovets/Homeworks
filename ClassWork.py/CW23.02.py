#класс человек с методом say.
class Human:
    def say(message): 
        return print (message)
    
    def age(number):
        if number < 10:
            print ("Младше 10-ти лет")
        else:
            print ("Старше 10-ти лет")
number = int(input("Введите возраст:"))
a = Human
a.say("HI")      
a.say("By")
a.age(number)


    
