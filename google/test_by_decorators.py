def check_one(func):
    def wrapper(n1, n2):
        # 1. Вызываем функцию и получаем строку "result=1" или другую
        res_str = func(n1, n2) 
        
        pure_result = n1 - n2

        if pure_result == 1:
        
            return "Ура мы получили единицу!"
    
    return wrapper
@check_one
def calculator(number_1, number_2):
    result = number_1 - number_2
    return f"{result=}"

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

print(calculator(number_1, number_2))