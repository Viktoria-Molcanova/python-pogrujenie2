def my_func(**kwargs) -> dict:
    return {v if isinstance(v, (int, str, float)) else str(v): k for k, v in kwargs.items()}


def main():
    print(my_func(first=1, second="two", third=3, fourth=[2, 2], fifth="five"))


if __name__ == "__main__":
    main()
