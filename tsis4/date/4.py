import datetime
date1 = datetime.datetime.now()
date2 = datetime.datetime.now() + datetime.timedelta(days=1)

delta = date2 - date1
print(delta.total_seconds())