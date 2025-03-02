try:
   a = input("Введите число:")
   c = input('Введите другое число:')
   d = input("Выберие действие 1) *, 2) /, 3) +, 4) -:")
   chi1 = float(a)
   chi2 = float(c)
   deys = int(d)
   if deys >= 5:
      print ('Ошибка: Действия от 1 до 4')
   if deys == 1:
      otvet1 = chi1 * chi2
      print (otvet1)
   elif deys == 2:
      otvet2 = chi1 / chi2
      print (otvet2)
   elif deys == 3:
      otvet3 = chi1 + chi2
      print (otvet3)
   elif deys == 4:
      otvet4 = chi1 - chi2
      print (otvet4)
except ValueError:
   print ('Ошибка: Нужно ввести число')
except ZeroDivisionError:
   print ('Ошибка: деление на ноль')