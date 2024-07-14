def generate_premium_dict(names, rates, bonuses):
    try:
        premium_dict = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
        return premium_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


names = ["Иван", "Алевтина", "Пётр"]
rates = [100, 200, 185]
bonuses = ["10.5%", "8%", "12.5%"]
result_dict = generate_premium_dict(names, rates, bonuses)
print(result_dict)
