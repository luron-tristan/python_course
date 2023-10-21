import time

print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
                      # epoch = when your computer thinks time began (refence point)

# print(time.ctime(1000000))

# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# print(time_object)
# utc_time_object = time.gmtime()
# print(utc_time_object)
# format = "%B %d %Y %H:%M:%S"
# local_time = time.strftime(format, time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# # (year, month, day, hours, minutes, seconds, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# time_string = time.mktime(time_tuple)
# print(time_string)