def main():

    user_input = input("What time is it? ")
    check_foodtime_24hr(convert(user_input))


def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes) / 60

def check_foodtime_24hr(time):
    breakfast_24h = range(7, 9) # between 07:00 and 8:00
    lunch_24hr = range(12, 14)  # between 12:00 and 13:00
    dinner_24hr = range(18, 20) # between 18:00 and 19:00

    time = int(time)

    if time in breakfast_24h:
        print("breakfast time")
    elif time in lunch_24hr:
         print("lunch time")
    elif time in dinner_24hr:
        print("dinner time")
    else:
        print("")


if __name__ == "__main__":
    main()