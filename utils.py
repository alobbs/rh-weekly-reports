import datetime


#
# Dates management
#

MONDAY_N = 0
FRIDAY_N = 4

def get_next_day_date(day):
    today = datetime.date.today()

    next_day = today
    while next_day.weekday() != day:
        next_day = next_day + datetime.timedelta(1)

    return next_day

def get_next_monday():
    return get_next_day_date(MONDAY_N)

def get_next_friday():
    return get_next_day_date(FRIDAY_N)


if __name__ == '__main__':
    print "Next Friday", get_next_monday()
    print "Next Monday", get_next_friday()
