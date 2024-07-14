from fractions import Fraction

def operate_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    sum_fraction = Fraction(num1, den1) + Fraction(num2, den2)
    product_fraction = Fraction(num1, den1) * Fraction(num2, den2)

    return sum_fraction, product_fraction


fraction1 = "1/2"
fraction2 = "1/3"
sum_result, product_result = operate_fractions(fraction1, fraction2)
print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")