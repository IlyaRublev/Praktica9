print("Задание 1")
def factorial(n):
    if n==1:
        return 1
    else:
        return (n * factorial(n-1))
n = int(input("Введите число: "))
print("Факториал числа равен: ")
print(factorial(n))

print("Задание 2")
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Введите число: "))
print(fibonacci(n))


