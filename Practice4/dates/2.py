from datetime import date, timedelta

current_date = date.today()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(yesterday)
print(current_date)
print(tomorrow)