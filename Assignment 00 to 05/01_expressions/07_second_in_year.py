# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):



# Constants for days, hours, minutes, and seconds
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate the number of seconds in a year by multiplying the number of days in a year by the number of hours in a day by the number of minutes in an hour by the number of seconds in a minute
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()