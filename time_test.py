import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.time())

print(time.localtime())

print(time.strptime("2022-07-07 12:30:00", "%Y-%m-%d %H:%M:%S"))
