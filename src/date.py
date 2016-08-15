#   coding=UTF_8
#
#   date.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

def isLeapYear(year):
            if year % 400 == 0:
                return True
            if year % 4 == 0 and year % 100 != 0:
                return True
            return False

## class for simple date calculations
class Date():

    def __init__(self, year = 0, month = 1, day = 1):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        if other == None:
            return False
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        # year
        if self.year < other.year:
            return True
        elif self.year == other.year:

            # month
            if self.month < other.month:
                return True
            elif self.month == other.month:

                # day
                if self.day < other.day:
                    return True
                else:
                    return False

            else:
                return False

        else:
            return False

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def weekdayIntToStr(self, wdi):
        if wdi == 2:
            return "Monday"
        if wdi == 3:
            return "Tuesday"
        if wdi == 4:
            return "Wendsday"
        if wdi == 5:
            return "Thursday"
        if wdi == 6:
            return "Friday"
        if wdi == 0:
            return "Saturday"
        if wdi == 1:
            return "Sunday"

    def offsetDay(self, integer):
        return integer -2

    def offsetMonth(self, integer):
        if integer == 1:
            return 1
        if integer == 2:
            return 4
        if integer == 3:
            return 4
        if integer == 4:
            return 0
        if integer == 5:
            return 2
        if integer == 6:
            return 5
        if integer == 7:
            return 0
        if integer == 8:
            return 3
        if integer == 9:
            return 6
        if integer == 10:
            return 1
        if integer == 11:
            return 4
        if integer == 12:
            return 6

    def offsetCentury(self, c):
        century = int(c/100) % 4
        if century == 0:
            return -1
        if century == 1:
            return 4
        if century == 2:
            return 2
        if century == 3:
            return 0

    def offsetYear(self, year):
        decade = year % 100

        first =  int(decade / 12)
        secound = (decade % 12)
        third = int(secound / 4)

        return first + secound + third

    def calculateWeekday(self):
        releap = 0
        if isLeapYear(self.year):
            if self.month == 1 or self.month == 2:
                #print("releaped")
                releap = -1
        return (self.day + self.offsetMonth(self.month) + self.offsetYear(self.year) + releap + self.offsetCentury(self.year)) % 7

    def set(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        return self

    def getDate(self):
        self.update()
        return (self.year, self.month, self.day)

    def getDateAsString(self):
        return "0"*(2-len(str(self.day))) + str(self.day) + "." + "0"*(2-len(str(self.month))) + str(self.month) + "." + "0"*(4-len(str(self.year))) + str(self.year)

    def getWeekday(self):
        self.update()
        return self.weekdayIntToStr(self.calculateWeekday())

    def printDate(self):
        # self.update() is implicit
        print(self.getDate(), ",", self.getWeekday())
        return self

    def update(self):
        self.addDay(0)
        return self

    def addDay(self,day=1):
        self.day += day
        if self.month == 2:
            if self.day > 28:
                if isLeapYear(self.year):
                    if self.day > 29:
                        self.day = self.day - 29
                        self.addMonth()
                        self.addDay(0)
                else:
                    self.day = self.day - 28
                    self.addMonth()
                    self.addDay(0)

        if self.month == 4 or self.month == 6 or self.month ==  9 or self.month == 11:
            if self.day > 30:
                self.day = self.day - 30
                self.addMonth()
                self.addDay(0)

        else:
            if self.day > 31:
                self.day = self.day - 31
                self.addMonth()
                self.addDay(0)


    def addMonth(self, month = 1):
        self.month += month
        if self.month > 12:
            self.month = self.month - 12
            self.addYear()
            self.addMonth(0)


    def addYear(self, year = 1, month = 0, day = 0):
        self.year += year

    def add(self, days=0, months=0, years=0):
        self.addYear(years)
        self.addMonth(months)
        self.addDay(days)
