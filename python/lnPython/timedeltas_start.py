#example file ofr working with timedelta objects

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta

def main():
   #construct basic timedelta and print it
   print timedelta(days=365,hours=5,minutes=1)

   #print today's date one year from now
   print "one year from now it will be:" + str(datetime.now() + timedelta(days=365))

   #create a timedelta taht uses more than one argument
   print "in two weeks and 3 days it will be:" + str(datetime.now()+timedelta(weeks=2,days=3))

   #calculate the date 1 week ago, formatted as a string
   t = datetime.now() - timedelta(weeks=1)
   s = t.strftime("%A %B %d,%Y")
   print "one week ago it was "+s

   ### how many days until April Fools' Day?
   today = date.today()
   afd = date(today.year,4,1)
   if afd <today:
      print "April Fool's day already went by %d days ago" %((today-afd).days)
      afd = afd.replace(year=today.year+1)

   #now calculate the amount of time until April Fool's day
   time_to_afd = abs(afd - today)
   print time_to_afd.days, "days until next April Fools' Day"

if __name__ == '__main__':
    main()