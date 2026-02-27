from datetime import datetime

date1 = datetime(2026, 2, 27, 13, 0, 0)
date2 = datetime(2026, 2, 19, 14, 0, 0)

diff = date1 - date2
seconds = diff.total_seconds()

print(seconds)