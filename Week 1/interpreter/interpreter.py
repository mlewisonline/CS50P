def main():
    try:
        X, Y, Z = input("Expression: ").split(' ')
        print(lets_do_some_math(X,Y,Z))
    except:
        print("please enter expression in format: 1 + 1")


def lets_do_some_math(x,y,z):
    match y:
        case '+':
            return float(x) + float(z)
        case '-':
            return float(x) - float(z)
        case '*':
            return float(x) * float(z)
        case '/':
            return float(x) / float(z)


main()