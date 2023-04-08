import random
import time
while True:
    start = time.time()
    print('У вас есть логин? 1-y | 0-n | 2-создать со своим поролем')
    print()
    answer1 = int(input())
    print()
    if answer1 == 0:
        login = input('Создайте логин: ')
        pas = ''
        for x in range(10000000):
            pas = pas + random.choice(list('10234567890'
                'qwertyuiopasdfghjklzxcvbnm'
                'QWERTYUIOPASDFGHJKLZXCVBNM'
                ',.<>!@#$%^&*)(}{]['))
        with open(login + '.ru', 'w') as file:
            file.write(pas)
    if answer1 == 2:
        login = input('Создайте логин: ')
        pas = input('Создайте пароль: ')
        with open(login + '.ru', 'w') as file:
            file.write(pas)
    if answer1 == 1:
        login = input('Введите логин: ')
        pas = open(login + '.ru', 'r').read()
    print('Ваш логин: ' + login)
    print('Ваш пароль: ' + pas)
    end = time.time() - start
    print(end)
    input()
