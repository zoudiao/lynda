from datetime import date
from datetime import time
from datetime import datetime

def main():
    #Date objects
    #Get today's date from the simple today() method from the date class
    today = date.today()
    print "Today's date is ", today

    #print out the date's individual components
    print "Date Components: ", today.day, today.month, today.year

    # retrieve today's weekday (0=Monday,6=Sunday)
    print "Today's Weekday #:", today.weekday()

    #get today's date from the datetime class
    today = datetime.now()
    print "The current date and time is:", today

    #Get the current time
    t = datetime.time(datetime.now())
    print "The current time is ",t

    #weekday return 0 (monday)trhough 6 (sunday)
    wd = date.weekday(today)

    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print "Today is day number %d" % wd
    print "Which is a " +days[wd]

if __name__ == '__main__':
    main()
