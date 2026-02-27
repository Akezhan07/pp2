from datetime import datetime 

current = datetime.now()

without_micro = current.replace(microsecond=0)
print(without_micro)