def main():

    vend_a_coke()


def vend_a_coke():
    coke_price = 50
    inserted_coin = 0
    accepted_coins = [5, 10, 25]

    while coke_price > 0:
        print(f"Amount Due: {coke_price}")
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin in accepted_coins:
            coke_price = coke_price - inserted_coin
        else:
            print(f"Amount Due: {coke_price}")
    print(f"Change Owed: {coke_price * -1}")

main()