from datetime import datetime

today = datetime.now()

def format_date(date):
    birth_date = str(date)[15:-3].split(',')
    year = int(birth_date[0])
    month = int(birth_date[1])
    day = int(birth_date[2])
    return year, month, day

def check_date(date, student_name):
    birthday = datetime(*date)

    if today.month == birthday.month:
        if today.day == birthday.day:
            return "{}'s birthday is today".format(student_name)
        elif today.day - 3 <= birthday.day < today.day:
            period =  today.day - birthday.day
            return "{}'s birthday was {} days ago".format(student_name, period)
        elif today.day < birthday.day <= today.day + 3:
            period =  birthday.day - today.day
            return "{}'s birthday will be in {} days".format(student_name, period)
        else:
            return "Birthday is not today, wasn't in 3 days ago and will not be in 3 days in future"
    else:
        return "Birthday is not today, wasn't in 3 days ago and will not be in 3 days in future"