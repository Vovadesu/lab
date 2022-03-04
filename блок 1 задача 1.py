
time = int(input("Введите время в секундах: "))

if (time <= 0) : 
    print("Ошибка: число должно быть положительным!") 
else :
    hours = time // 3600
    mins = (time - (hours * 3600)) // 60
    sec = time - (hours * 3600) - (mins * 60)
    print("Время в формате 'часы:минуты:секунды': \n", hours, ":", mins, ":",
      sec, sep="")
