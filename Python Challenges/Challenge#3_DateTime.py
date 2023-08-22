import datetime #This gives us access to the datetime modules
import pytz #This gives us access to different time zones
 
#Each of the variables are set with a specific timezone
Portland = 'US/Pacific'
New_York_City = 'US/Eastern'
London = 'Europe/London'

#This function will get us a current time for each zone
def Get_Current_Time(timezone):
    x = datetime.datetime.now(pytz.timezone(timezone))
    return x.strftime('%H:%M %p')

#This will compare whether they are open or close
def Compare(x):
    GCT = Get_Current_Time(x)
    if GCT  > '09:00' and GCT   < '17:00':
        return("We are open!")
    else:
        return("We are closed!")

#This gives us 12-hr time
def Change_Time(timezone):
    y = datetime.datetime.now(pytz.timezone(timezone))
    return y.strftime('%I:%M %p')

print('It is ' + Change_Time(Portland) + ' in Portland and ' + Compare(Portland))
print('It is ' + Change_Time(New_York_City) + ' in New York City and ' + Compare(New_York_City))
print('It is ' + Change_Time(London) + ' in London and ' + Compare(London))


