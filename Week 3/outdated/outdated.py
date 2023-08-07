def main():
    print(get_user_date())

'''Take a date input of MM-DD-YYYY format and return an ISO 8601 formatted date string.'''
def short_date_to_iso(month, day, year):
    try:
       # month, day, year = date.split("/")
        if int(month) in range(1,13) and int(day) in range(1,32):
            #output YYYY-MM-DD
            return (f"{int(year)}-{int(month):02}-{int(day):02}")
    except ValueError:
        return None

'''Take a date input of Month Day, Year and return an ISO 8601 formatted date string.'''
def long_date_to_iso(month, day, year):
    months = ["January", "February", "March","April","May","June","July","August","September","October","November","December"]
    try:
        if  month in months and int(day) in range(1,32):
            #output YYYY-MM-DD
            return (f"{int(year)}-{int(months.index(month)+1):02}-{int(day):02}")
    except ValueError:
        return None

'''Get user input and format it for processing.'''
def get_user_date():
    while True:
        date = input("Date: ").strip()
        # Try to get date in first format
        try:
            month, day, year = date.split("/")
            result = short_date_to_iso(month, day, year)
            if result is not None:
                return result
            else:
                raise ValueError
        except ValueError:
            pass
        # Try to get date in second format
        try:
            month, day, year = date.split(" ")
            # strip the trailing comma from the day
            if day.endswith(","):
                day = day.strip(",")
            else:
                raise ValueError
            result = long_date_to_iso(month,day,year)
            if result is not None:
                return result
            else:
                raise ValueError
        except ValueError:
            pass

if __name__ == "__main__":
    main()
