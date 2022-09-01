# print(11111 * 1111111)
#
# # print((42)/(4 + 2 * (-2)))
#
# print(2014.0 ** 14)
#
# print(1.2345e-3)
#
# print(7//3)
#
# print(int(2.99))
#
# print(int(-1.6))
#
# print(9 ** 19 - int(float(9  ** 19)))
#
# print(type(['fuck']))
#
# # x = int(input())
# # h = int(input())
# # m = int(input())
# #
# # c = x + (h * 60 + m)
# #
# # print(c // 60)
# # print(c % 60)
#
# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)


# A = int(input())  #мин сна
# B = int(input())  #макс сна
# H = int(input())  #cпит сейчас
#
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# else:
#     print('Пересып')


# A = int(input())  #номер года
#
# if (A % 4 == 0) and (A % 100 != 0) or (A % 400 == 0):
#     print('Високосный')
# else:
#     print('Обычный')
#

# print("239" < "30" and 239 < 30)
# print("239" < "30" and 239 > 30)
# print("239" > "30" and 239 < 30)
# print("239" > "30" and 239 > 30)
#
# print ("123" + "42")

# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b +c)/2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)
# (−15,12]∪(14,17)∪[19,+∞)
# a = int(input())
# if -15<a<=12 or 14<a<17 or a>=19:
#     print('True')
# else:
#     print('False')

# a = float(input())
# b = float(input())
# c = (input())
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == 'pow':
#     print(a ** b)
# elif c == '/' and b != 0:
#     print(a / b)
# elif c == 'mod' and b != 0:
#     print(a % b)
# elif c == 'div' and b != 0:
#     print(a // b)
# else:
#     print("Деление на 0!")


# operations = {
#       "+": lambda x, y: x + y,
#       "-": lambda x, y: x - y,
#       "/": lambda x, y: x / y,
#       "*": lambda x, y: x * y,
#       "mod": lambda x, y: x % y,
#       "pow": lambda x, y: x ** y,
#       "div": lambda x, y: x // y
# }
#
# x, y = float(input()), float(input())
# operation = input()
#
# if operation in ["mod", "div", "/"] and y == 0:
#     print("Деление на 0!")
# else:
#     print(operations[operation](x, y))

# room = input()
# if room == 'треугольник':
#     a = (int(input()))
#     b = (int(input()))
#     c = (int(input()))
#     p = (a + b + c)/2
#     print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif room == 'квадрат':
#     a = (int(input()))
#     b = (int(input()))
#     print(a * b)
# elif room == 'круг':
#     r = (int(input()))
#     pi = 3.14
#     print(pi * r ** 2)

# a = (int(input()))
# b = (int(input()))
# c = (int(input()))
#
# print(max(a, b, c))
# print(min(a, b, c))
# print((a + b + c) - ((max(a, b, c) + (min(a, b, c)))))

# a = int(input())
# b = 'программист'
# if a%10==1 and not a%100==11:
#     print(a, b)
# elif 1<a%10<5 and not 10<a%100<15:
#     print(a, b + 'а')
# else:
#     print(a, b + 'ов')

# a = input()
# sum1 = int(a[0]) + int(a[1]) + int(a[2])
# sum2 = int(a[3]) + int(a[4]) + int(a[5])
# if sum1 == sum2:
#     print('Счастливый')
# else:
#     print('Обычный')


# a = 5
# while a > 0:
#     print (a, end = ' ')
#     a += 1

# i = 0
# while i <= 10:
#     print('Итерация')
#     i = i + 1
#     if i > 7:
#         i = i + 2
#
# print(i)
# n = int(input())
# c = 1
# while c <=n:
#
#     print('*' * c)
#     c += 1

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


# s = 0
# c = int(input())
# while c != 0:
#     s += c
#     c = int(input())
# print(s)


# a = int(input())
# b = int(input())
# s = 1
# k = 2
# while s < k:
#     if s % a == 0 and s % b ==0
#         k = s
#     else:
#         k = k + 1
#         s = s +1
# print(s)
#

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

# a = 0
# while a<=100:
#     a = int(input())
#     if a > 100:
#         break
#     if a > 10:
#         continue
#     print(a)

# n = int(input())
# for i in range(n):
#     for j in range (n):
#         print('*', end='')
#     print()

# a = input()
# c1 = a.upper().count('C')
# c2 = a.upper().count('G')
#
# s = ((c1 + c2)/len(a)) * 100
# print(s)

#palindrome

# a1 = input().upper()
# a = 'a' * 1000000
# s1 = a
# s2 = a[::-1]
# if s1 == s2:
#     print('YES, it a palindrome!')
# else:
#     print('FUCK YOU!')

# string = input()
# counter = 1
# i = 0
#
# while (i + 1) < len(string):
#     if string[i] == string[i + 1]:
#         counter += 1
#     else:
#         print(string[i] + str(counter), end='')
#         counter = 1
#
#     i += 1
#
# print(string[i] + str(counter))

# a = [int(i) for i in input().split()]
# sum = sum(a)
# # l = len(a) - 1
# # for i in range(0, l + 1):
# #     sum = sum + a[i]
# print(sum)

def f(n):
    return n * 10 + 5
print(f(f(f(10))))