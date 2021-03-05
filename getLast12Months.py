from datetime import date

def getLast12Months():
    today = date.today()
    todayMonth = today.month
    todayYear = today.year
    c = 0
    lst = []
    while(c<12):
        lst.append((todayYear, todayMonth))
        if todayMonth == 1:
            todayYear -= 1
            todayMonth = 12
        else:
            todayMonth -= 1
        c += 1
    return lst
