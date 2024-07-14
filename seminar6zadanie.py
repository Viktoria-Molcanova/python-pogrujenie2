# Модуль с проверкой даты с возможностью запуска в терминале
import sys
from datetime import datetime
import random
def check_date(input_date):
    try:
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')
        print("Дата {} введена корректно.".format(input_date))
    except ValueError:
        print("Ошибка! Некорректный формат даты. Используйте формат YYYY-MM-DD.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        date_input = sys.argv[1]
        check_date(date_input)
    else:
        print("Пожалуйста, введите дату для проверки в формате YYYY-MM-DD.")

# Шахматный модуль с решением задачи о 8 ферзях

def check_queens(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            if queens_positions[i][0] == queens_positions[j][0] or queens_positions[i][1] == queens_positions[j][1] or abs(queens_positions[i][0] - queens_positions[j][0]) == abs(queens_positions[i][1] - queens_positions[j][1]):
                return False
    return True

def generate_random_queens():
    successful_arrangements = 0
    while successful_arrangements < 4:
        queens_positions = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
        if check_queens(queens_positions):
            print("Успешная расстановка ферзей:", queens_positions)
            successful_arrangements += 1

if __name__ == "__main__":
    generate_random_queens()
