# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1

# n=int(input('Введите трехзначное число: '))
# sum=0
# while n>0:
#     x=n%10
#     sum=sum+x
#     n=n//10
# print(f'Для числа {n} сумма цифр будет {sum}')  

# Вариант 2

# n=int(input('ВВедите трехзначное число: '))
# a=int(input('Введите первую цифру числа: '))
# b=int(input('Введите вторую цифру числа: '))
# c=int(input('Введите третью цифру числа: '))
# sumn=a+b+c
# print(f'Для числа {n} сумма цифр равна {sumn}: {a}+{b}+{c}')


# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

# zur=int(input('Введите общее количество журавликов: '))
# x=zur//6
# Ket=(x+x)*2
# print(f'Если дети сделали вместе {zur} журавликов, то Петя сделал {x} журавлика, Сергей {x} журавлика, а Катя {4}')

# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

# n=int(input('Введите номер билета: '))
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# sum1=a+b+c
# sum2=d+e+f
# if sum1==sum2:
#     print('Yes')
# else:
#     print('No')    

# Тернарный оператор
# print('Yes' if sum1==sum2 else 'No')


# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

# n=int(input('Введите длину шоколадки '))
# m=int(input('Введите ширину шоколадки '))
# k=int(input('Введите сколько долек хотите отломить от шоколадки '))
# if k%2==0:
#     print('Yes')
# else:
#     print('No')   



