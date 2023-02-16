first_var = float(input("Введите первое число:"))
second_var = float(input("Введите второе число:"))
operation = input("Выберите тип операции: '+','-','*','/' : ")

if (operation == '+'):
    print(first_var + second_var)
elif(operation == '-'):
    print(first_var - second_var)
elif (operation == '*'):
    print(first_var * second_var)
elif (operation == '/'):
    print(first_var / second_var)
print("Внес изменения для проверки коммита")