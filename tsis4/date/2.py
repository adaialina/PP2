import datetime
today = datetime.datetime.now()
print("Today: ", today)

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print("Yesterday: ", yesterday)

tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
print("Tomorrow: ", tomorrow)