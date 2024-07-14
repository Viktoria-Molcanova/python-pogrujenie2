def fibonacci_generator(n):
    try:
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    except Exception as e:
        print(f"Ошибка: {e}")


n = 10
fibonacci_sequence = [num for num in fibonacci_generator(n)]
print(f"Последовательность  {n} чисел:", fibonacci_sequence)
