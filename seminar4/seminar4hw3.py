p = 0.015  # процент за снятие
o = 3  # количество последовательных операций для начисления %
a = 0.03  # процент пополнения карты
min_p = 30  # минимум удержания
max_p = 600  # максимум удержания
min_b = 50  # минимальная купюра
min_t = 5_000_000  # налогооблагаемая сумма
tax = 0.1  # ставка налогообложения

operation_log = []

def perform_operation(action: str, balance: float) -> float:
    if action == "снять":
        amount = float(input("Сумма для снятия: "))
        if amount > balance:
            print("Ошибка: недостаточно средств для снятия!")
            return balance
        if amount < min_b:
            print(f"Ошибка: минимальная купюра для снятия составляет {min_b}!")
            return balance
        balance -= amount * (1 + p)  # учитываю процент за снятие
        operation_log.append(f"Снятие: {amount:.2f} - Успешно")
    elif action == "пополнить":
        amount = float(input("Сумма для пополнения: "))
        if amount < min_p:
            print(f"Ошибка: минимальная сумма пополнения составляет {min_p}!")
            return balance
        balance += amount * (1 + a)  # учитываю процент пополнения
        operation_log.append(f"Пополнение: {amount:.2f} - Успешно")

    print(f"Баланс обновлен: {balance:.2f}")
    return balance


def main():
    balance = 0.0

    while True:
        action = input("Введите действие (снять/пополнить/баланс/выход): ")
        if action in ["снять", "пополнить"]:
            balance = perform_operation(action, balance)
        elif action == "баланс":
            print(f"Баланс счета: {balance:.2f}")
        elif action == "выход":
            break
        else:
            print("Ошибка: неверное действие. Пожалуйста, попробуйте снова.")

    print("-- логи --")
    for o in operation_log:
        print(o)


if __name__ == "__main__":
    main()
