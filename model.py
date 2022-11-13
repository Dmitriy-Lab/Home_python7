
names = ['Иванов Иван Иванович', 'Боброва Оксана Сергеевна', 'Степашкина Маруся Олеговна']
tel = ['+79120057895\n','+79225481255\n','+79015731279\n']


def addTel():
    global names
    global tel

    name = input("Введите ФИО: ")
    telephone = input("Введите tel: ") + '\n'

    names.append(name)
    tel.append(telephone)
    return 'Файл обновлен, для проверки выведите справочник'


def printTel():
    global names
    global tel

    list =[]
    for i in range(len(names)):
        list.append(names[i])
        list.append(tel[i])

    return ' '.join(list)


def saveAsHTML():
    global names
    global tel

    book = open('book.html', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])

    return 'Файл "book.html" сохранен на вашем компьютере'

def saveAsXML():
    global names
    global tel

    book = open('book.xml', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])

    return 'Файл "book.xml" сохранен на вашем компьютере'