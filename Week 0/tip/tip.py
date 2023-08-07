def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    _, amount = d.split('$')
    amount = float(amount)
    return round(amount,2)



def percent_to_float(p):
    amount, _ = p.split('%')
    amount = float(amount) / 100
    return float(amount)

main()