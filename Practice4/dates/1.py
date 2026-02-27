from datetime import date, timedelta

current_date = date.today()
new_date = current_date - timedelta(days=5)

print(new_date)