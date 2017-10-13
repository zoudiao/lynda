#example file for working with Calendars

import calendar
#create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2017,1,0,0)
print str

hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2017,1)
print str

for i in c.itermonthdays(2017,10):
    print i

for day in calendar.day_name:
    print day


for m in range(1,13):
    cal = calendar.monthcalendar(2017,m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] !=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print "%10s %2d" % (calendar.month_name[m],meetday)