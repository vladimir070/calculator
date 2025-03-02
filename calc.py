try:
   a = input("Введите число:")
   c = input('Введите другое число:')
   d = input("Выберие действие 1) *, 2) /, 3) +, 4) -:")
   number1= float(a)
   number2= float(c)
   choice= int(d)
   if choice >= 5:
      print ('Ошибка: Действия от 1 до 4')
   if choice == 1:
      solution1 = number1 * number2
      print (solution1)
   elif choice == 2:
      solution2 = number1 / number2
      print (solution2)
   elif choice == 3:
      solution3 = number1 + number2
      print (solution3)
   elif choice == 4:
      solution4 = number1 - number2
      print (solution4)
except ValueError:
   print ('Ошибка: Нужно ввести число')
except ZeroDivisionError:
   print ('Ошибка: деление на ноль')
