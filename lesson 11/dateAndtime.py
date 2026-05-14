import datetime

currentDate= datetime.datetime.now()

print("year:" , currentDate.year)
print("month:" , currentDate.month)
print("day:" , currentDate.day)
print("hour:" , currentDate.hour)
print("minute:" , currentDate.minute)
print("second:" , currentDate.second)
print("microsecond:" , currentDate.microsecond)

print("--------------------")

currentDate2= datetime.datetime.now().date()


print("year" , currentDate2.year )
print("day" , currentDate2.day )
print("month" , currentDate2.month )


print("------------------")

timeObject = datetime.time(12,30,45,123456)

print("hour", timeObject.hour)
print("minute", timeObject.minute)
print("second", timeObject.second)
print("microsecond", timeObject.microsecond)


print("------------")




specific_datetime = datetime.datetime(2024,1,1,12,25,1,2255)

formatdate = specific_datetime.strftime('%d-%m-%Y')

print(formatdate)

print("------------")

utc_time = datetime.datetime.now(datetime.timezone.utc)

print("current timie:" , utc_time)


custom = datetime.timedelta(hours=3)