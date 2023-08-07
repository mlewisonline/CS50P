def main():



    orders()

def orders():
    products ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    sub_total = 0
    while True:
        try:
            item = input("Item: ").capitalize().title()
            if item in products.keys():
                sub_total += float(products[item])
                print(f"Total: ${sub_total:.2f}")
                #print("Total:"+" $" + sub_total)
            elif item not in products.keys():
                pass
        except EOFError:
            quit()

if __name__ == "__main__":
    main()