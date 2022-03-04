

num = int(input("Введите положительное число: "))
max_digit = 0 
temp = 0

if (num < 0):
    print("Это число отрицательное!")
else:
    while(num > 0):               # ищем остаток от числа, пока оно больше нуля
        temp = num % 10
        if (temp > max_digit):
            max_digit = temp    
        num = num // 10
    print("Самая большая цифра в числе:", max_digit)    