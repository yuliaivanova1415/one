print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n.isdigit() and int(n) > 1:
        return True
    else:
        return False
while True:
    print('Придумайте правую границу для случайного выбора числа (от 1 до n). Введите n:')
    n = input()
    if is_valid(n) == True:
        n = int(n)
        break
    else:
        print('Введите целое число больше 1')  
import random
ranum = random.randrange(1, n)
count = 0
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= n:
        return True
    else:
        return False
while True:
    print('Введите число от 1 до', n, ':')
    num = input()
    count += 1
    if is_valid(num) == True:
        num = int(num)
        if num < ranum:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if num > ranum:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if num == ranum:
            print('Вы угадали, поздравляем!')
            print('Количество ваших попыток :', count)
            break        
    else:
        print('А может быть все-таки введем целое число от 1 до', n, '?')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

input()





    
