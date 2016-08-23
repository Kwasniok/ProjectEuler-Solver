#   coding=UTF_8
#
#   date.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

def is_leap_year(year):
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

    # string related methods

    def __str__(self):
        # self.update() is implicit
        return str(self.get_date()) +  "," + str(self.get_weekday())

    def __repr__(self):
        return str(self.get_date()) +  "," + str(self.get_weekday())

    def __unicode__(self):
        return unicode(self.get_date()) +  "," + unicode(self.get_weekday())

    def weekday_to_str(self, wdi):
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

    def offset_day(self, integer):
        return integer -2

    def offset_month(self, integer):
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

    def offset_century(self, c):
        century = int(c/100) % 4
        if century == 0:
            return -1
        if century == 1:
            return 4
        if century == 2:
            return 2
        if century == 3:
            return 0

    def offset_year(self, year):
        decade = year % 100

        first =  int(decade / 12)
        secound = (decade % 12)
        third = int(secound / 4)

        return first + secound + third

    def calculate_weekday(self):
        releap = 0
        if is_leap_year(self.year):
            if self.month == 1 or self.month == 2:
                #print("releaped")
                releap = -1
        return (self.day + self.offset_month(self.month) + self.offset_year(self.year) + releap + self.offset_century(self.year)) % 7

    def set(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        return self

    def get_date(self):
        self.update()
        return (self.year, self.month, self.day)

    def get_date_as_string(self):
        return "0"*(2-len(str(self.day))) + str(self.day) + "." + "0"*(2-len(str(self.month))) + str(self.month) + "." + "0"*(4-len(str(self.year))) + str(self.year)

    def get_weekday(self):
        self.update()
        return self.weekday_to_str(self.calculate_weekday())

    def update(self):
        self.add_days(0)
        return self

    def add_days(self,day=1):
        self.day += day
        if self.month == 2:
            if self.day > 28:
                if is_leap_year(self.year):
                    if self.day > 29:
                        self.day = self.day - 29
                        self.add_months()
                        self.add_days(0)
                else:
                    self.day = self.day - 28
                    self.add_months()
                    self.add_days(0)

        if self.month == 4 or self.month == 6 or self.month ==  9 or self.month == 11:
            if self.day > 30:
                self.day = self.day - 30
                self.add_months()
                self.add_days(0)

        else:
            if self.day > 31:
                self.day = self.day - 31
                self.add_months()
                self.add_days(0)


    def add_months(self, month = 1):
        self.month += month
        if self.month > 12:
            self.month = self.month - 12
            self.add_years()
            self.add_months(0)


    def add_years(self, year = 1, month = 0, day = 0):
        self.year += year

    def add(self, days=0, months=0, years=0):
        self.add_years(years)
        self.add_months(months)
        self.add_days(days)
