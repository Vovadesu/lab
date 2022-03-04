


month = int(input("Введите номер месяца (от 1 до 12): "))

if (month > 12):
    print("Число больше 12!")
elif (month < 0):
    print("Число меньше нуля!")
elif (month == 12 or month == 1 or month == 2):
    print("Это зима!")    
elif (month == 3 or month == 4 or month == 5):
    print("Это весна!")
elif (month == 6 or month == 7 or month == 8):
    print("Это лето!")
elif (month == 9 or month == 10 or month == 11):
    print("Это осень!")  
              