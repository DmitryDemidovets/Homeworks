'''
Задача 4

Поставить в соответствие следующим английским символам русские буквы:
h - х,
e - е,
l - л,
o - о,
w - в,
r - р,
d - д
и преобразовать строку «hello world!» в русские символы
'''
latin: str = 'helowrd' 
cyrillic: str = 'хеловрд'
abc: dict = dict(zip(latin, cyrillic))

text: str = 'hello world!'

def translit(text: str, abc: dict) -> str:
    new_text: str = '' 
    for i in text:
        if i in abc.keys(): 
            new_text = new_text + abc.get(i) 
        else:
            new_text += i
    return new_text

print(translit(text, abc))