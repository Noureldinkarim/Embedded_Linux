import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

if month < 1 or month>12:
    print("Invalid dates")
else:
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year,month)
    print(month_calendar)

