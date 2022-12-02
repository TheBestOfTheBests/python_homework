# a=input("Введите число а ")
# b=input("Введите число b ")
# c=input("Введите число c ")
# print(c,b,a)



# name="Иван"
# age=15
# nameyou=input("Как вас зовут? ")
# ageyou=input("Сколько вам лет? ")
# print("Привет, " +nameyou +" меня зовут "+name +".")
# print("Мне " +str(age) +" лет!")
# print("А вам, как я уже понял, " +ageyou +", круто, больше не чего сказать.")
# print("Вы хороший собеседник, но мне пора, удачи!")



# import math
# k1=input("Количество учеников в 1-ом кабинете: ")
# print()
# k2=input("Количество учеников в 2-ом кабинете: ")
# print()
# k3=input("Количество учеников в 3-ом кабинете: ")
# k11=float(int(k1)/2)
# p1=math.ceil(k11)
# k22=float(int(k2)/2)
# p2=math.ceil(k22)
# k33=float(int(k3)/2)
# p3=math.ceil(k33)
# vseparti=int(p1+p2+p2)
# print("Всего нужно купить " +str(vseparti) +" парт")


# Задания:
# 1)
# chislo1=int(input("Введите первое число: "))
# chislo2=int(input("Введите второе число: "))
# if chislo1>chislo2:
#     print(chislo2)
# elif chislo1<chislo2:
#     print(chislo1)
# else:
#     print("Они равны =)")


# 2)
# chislo1=int(input("Введите первое число: "))
# chislo2=int(input("Введите второе число: "))
# chislo3=int(input("Введите третье число: "))
# if chislo1>=chislo2>chislo3:
#      print(chislo3)
# elif chislo1<chislo2<=chislo3:
#     print(chislo1)
# elif chislo2<chislo1<=chislo3:
#     print(chislo2)
# else:
#     print("Они равны =)")


# 3)
# chislo1=int(input("Введите первое число: "))
# if chislo1>0:
#     print("1")
# elif chislo1<0:
#     print("-1")
# else:
#     print("0")


# 4)
# x1=int(input("Введите координату по оси x первой клетки: "))
# y1=int(input("Введите координату по оси y первой клетки: "))
# x2=int(input("Введите координату по оси x второй клетки: "))
# y2=int(input("Введите координату по оси y второй клетки: "))
# if (8 >= x1 > 0) and (8 >= y1 > 0) and(8 >= x2 > 0) and (8 >= y2 > 0): 
#     if (x1+y1+x2+y2)%2 == 0:
#         print()
#         print("Yes")
#     else:
#         print()
#         print("No")
# else:
#     print()
#     print("Введены неверные координаты")


# 5)
# ch1=int(input("Введите первое число: "))
# ch2=int(input("Введите второе число: "))
# ch3=int(input("Введите третье число: "))
# if ch1==ch2==ch3:
#     print()
#     print("3")
# elif ch1==ch2 or ch2==ch3 or ch1==ch3:
#     print()
#     print("2")
# else:
#     print()
#     print("0")


# 6)
# n=int(input("Введите количество долек по горизонтали: "))
# m=int(input("Введите количество долек по вертикали: "))
# k=int(input("Введите количество долек: "))
# vsego=int(n)*int(m)
# if vsego>k:
#     print("Yes")
# else:
#     print("No")


# 7) Ладья
# ch1=int(input("Введите столб 1-ой клетки (от 1 до 8): "))
# ch2=int(input("Введите строку 1-ой клетки (от 1 до 8): "))
# ch3=int(input("Введите столб 2-ой клетки (от 1 до 8): "))
# ch4=int(input("Введите строку 3-ой клетки (от 1 до 8): "))
# if ch1>ch3 or ch1<ch3:
#     if ch2==ch4:
#         print("Yes")
# elif ch1==ch3:
#     if ch2>ch4 or ch2<ch4:
#         print("Yes")
# else:
#     print("No")


# 8) Король
# x1=int(input("Введите координату по оси x первой клетки: "))
# y1=int(input("Введите координату по оси y первой клетки: "))
# x2=int(input("Введите координату по оси x второй клетки: "))
# y2=int(input("Введите координату по оси y второй клетки: "))
# if (8 >= x1 > 0) and (8 >= y1 > 0) and(8 >= x2 > 0) and (8 >= y2 > 0):
#     if abs(x1-x2) <=1 and abs(y1-y2) <=1:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("Вы что-то напутали")

# 9) Слон
# x1=int(input("Введите координату по оси x первой клетки: "))
# y1=int(input("Введите координату по оси y первой клетки: "))
# x2=int(input("Введите координату по оси x второй клетки: "))
# y2=int(input("Введите координату по оси y второй клетки: "))
# if (8 >= x1 > 0) and (8 >= y1 > 0) and(8 >= x2 > 0) and (8 >= y2 > 0):
#     if abs(x1-x2)==abs(y1-y2):
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("Вы что-то напутали")


# 10) Ферзь
# x1=int(input("Введите координату по оси x первой клетки: "))
# y1=int(input("Введите координату по оси y первой клетки: "))
# x2=int(input("Введите координату по оси x второй клетки: "))
# y2=int(input("Введите координату по оси y второй клетки: "))
# if (8 >= x1 > 0) and (8 >= y1 > 0) and(8 >= x2 > 0) and (8 >= y2 > 0):
#     if abs(x1-x2)==abs(y1-y2) or x1==x2 or y1==y2:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("Вы что-то напутали")


# 11) Конь
# x1=int(input("Введите координату по оси x первой клетки: "))
# y1=int(input("Введите координату по оси y первой клетки: "))
# x2=int(input("Введите координату по оси x второй клетки: "))
# y2=int(input("Введите координату по оси y второй клетки: "))
# if (8 >= x1 > 0) and (8 >= y1 > 0) and(8 >= x2 > 0) and (8 >= y2 > 0):
#     if (x1+1==x2 or x1-1==x2 or x1-2==x2 or x1+2==x2) and (y1+1==y2 or y1-1==y2 or y1-2==y2 or y1+2==y2):
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("Вы что-то напутали")
