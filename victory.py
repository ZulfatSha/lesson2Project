#МОДУЛЬ 6:
#Выбрать минимум 5 известных людей и узнать их год рождения.
# Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
#После того как пользователь ввел все ответы, программа считает и выводит на экран:
#- количество правильных ответов
#- количество ошибок
#- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
#- процент неправильных ответов
#После вывода информации программа спрашивает пользователя хочет ли он начать игру сначала,
# если да - то повторяем все сначала, если ответ нет - выходим из программы
# В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости
quantity = 0
error = 0
all_question = 5

celebrity_1 = input('В каком году родился Zinedin Zidane: ')
if celebrity_1 == '1972':
    print('Верно')
    quantity = quantity + 1
else:
    print('Не верно')
    error = error + 1

celebrity_2 = input('В каком году родился Sergey Semak: ')
if celebrity_2 == '1976':
    print('Верно')
    quantity = quantity + 1
else:
    print('Не верно')
    error = error + 1

celebrity_3 = input('В каком году родился Andrey Arshavin: ')
if celebrity_3 == '1981':
    print('Верно')
    quantity = quantity + 1
else:
    print('Не верно')
    error = error + 1

celebrity_4 = input('В каком году родился Gekdeniz Karadeniz: ')
if celebrity_4 == '1980':
    print('Верно')
    quantity = quantity + 1
else:
    print('Не верно')
    error = error + 1

celebrity_5 = input('В каком году родился Kurban Berdyev: ')
if celebrity_5 == '1952':
    print('Верно')
    quantity = quantity + 1
else:
    print('Не верно')
    error = error + 1

print(quantity, 'верных ответов из ', all_question, ' вопросов')
print(error, 'ошибочных ответов из ', all_question, ' вопросов')
correct_answers = (quantity * 100)/all_question
print(correct_answers, '% правильных ответов')
no_correct_answers = (error * 100)/all_question
print(no_correct_answers, '% неправильных ответов')