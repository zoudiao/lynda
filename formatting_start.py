from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    #control codes
    now = datetime.now()

    ### Date formatting ###
    #%y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print now.strftime("%Y") #full year with century
    print now.strftime("%y")
    print now.strftime("%a,%d %B,%y")

    #%c - locale's date and time , %x - locale's date, %X - locale's time
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")

   #%I/%H - 12/24 hour, %M - minutes, %S - second , %p - locale's AM/PM
    print now.strftime("%I:%M:%S %p")
    print now.strftime("%H:%M")

if __name__ == '__main__':
    main()


