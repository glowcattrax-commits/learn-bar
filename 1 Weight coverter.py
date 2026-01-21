weight = float(input("Введите вес"))
i = str(input(f"'K'g or 'L'bs?"))

if(i == "K" or i == "k"):
    print(f"Ваш вес в фунтах: {weight*2.205}.")
elif(i == "L" or i == "l"):
    print(f"Ваш вес в килограммах: {weight/2.205}.")
else:
    print("Введено неверное значение")