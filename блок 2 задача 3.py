s = input("Введите данные: ")   #
lis = (s.split()).copy()        # делаем копию списка, возвращенного методом split, чтобы не изменять сам список
cor = lis.copy()                #создаём копию списка, которую и будем изменять
i = 0

while (i < len(cor)-1):
    cor[i] = lis[i+1]
    cor[i+1] = lis[i]
    i = i + 2 
    
print(cor)

    
