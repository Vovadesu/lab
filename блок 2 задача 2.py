s = input("Введите вашу строку: ") # ввод самой строки в формате str
temp = s.split()                         # по разделителю " " разбиваем строку в список                                      
for i in range(0, len(temp)):            
    print(f"{i+1}. {temp[i]}")           # форматируем и выводим
        
