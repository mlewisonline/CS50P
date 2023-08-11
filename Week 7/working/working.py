import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = parse_input(s)
    if len(time) == 6:
       return long_time_convert(time)
    elif len(time) == 4:
        return short_time_convert(time)


def parse_input(s):
    pattern1 = r"^(\d?\d?):([0-5]+\d) (\w\w) to (\d?\d?):([0-5]+\d)? (\w\w)$"
    pattern2 = r"^(\d?\d?) (\w\w) to (\d?\d?) (\w\w)$"
    try:
        if re.search(pattern1, s, re.IGNORECASE):
            result = re.search(pattern1, s, re.IGNORECASE)
            return result.groups()
        elif  re.search(pattern2, s, re.IGNORECASE):
            result = re.search(pattern2, s, re.IGNORECASE)
            return result.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid input")


def long_time_convert(time):
    s_hours, s_mins, s_am_pm, e_hours, e_mins, e_am_pm = time
    s_hours = int(s_hours)
    e_hours = int(e_hours)
    if s_am_pm == 'PM' and s_hours != 12:
        s_hours += 12
    elif e_am_pm == 'PM' and e_hours != 12:
        e_hours += 12
    elif s_am_pm == 'AM' and s_hours == 12:
        s_hours = 0
    elif e_am_pm == 'AM' and e_hours == 12:
        e_hours = 0
    return (f'{s_hours:02d}:{s_mins} to {e_hours:02d}:{e_mins}')


def short_time_convert(time):
    s_hours, s_am_pm, e_hours, e_am_pm = time
    s_hours = int(s_hours)
    e_hours = int(e_hours)
    if s_am_pm == 'PM' and s_hours != 12:
        s_hours += 12
    elif e_am_pm == 'PM' and e_hours != 12:
        e_hours += 12
    elif s_am_pm == 'AM' and s_hours == 12:
        s_hours = 0
    elif e_am_pm == 'AM' and e_hours == 12:
        e_hours = 0
    return (f'{s_hours:02d}:00 to {e_hours:02d}:00')


if __name__ == "__main__":
    main()