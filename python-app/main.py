import calendar

print("Welcome to this sample supersonic calendar app")

year = int(input('enter year: '))
month = int(input('enter month: '))

print(calendar.month(year, month))
