def main():
    go_shopping()


def go_shopping():
    shopping_list ={}
    while True:
        try:
            item = input()
            #Build Shopping List
            if item in shopping_list:
                shopping_list[item] = int(shopping_list[item] + 1)
            else:
                shopping_list[item] = 1
        except EOFError:
            # Print Shopping List on exit
            for item, count in sorted(shopping_list.items()):
                print(f"{count} {str(item).upper()}")
            quit()


if __name__ == "__main__":
    main()