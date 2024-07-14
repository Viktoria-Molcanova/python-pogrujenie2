# Проверка существования треугольника и определение его типа
def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print("Треугольник - разносторонний")
        elif a == b == c:
            print("Треугольник - равносторонний")
        else:
            print("Треугольник - равнобедренный")
    else:
        print("Треугольник с такими сторонами не существует")

# Проверка числа на простоту или составность
def check_prime(num):
    if num <= 1 or num > 100000:
        print("Число не подходит для проверки")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Число составное")
                break
        else:
            print("Число простое")

# Игра угадай число
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print("Угадайте число от 0 до 1000. У вас 10 попыток.")
for _ in range(attempts):
    guess = int(input("Введите ваше предположение: "))
    if guess < secret_num:
        print("Больше")
    elif guess > secret_num:
        print("Меньше")
    else:
        print("Поздравляем! Вы угадали число.")
        break
