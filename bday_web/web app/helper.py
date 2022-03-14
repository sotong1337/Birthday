#######################################
# Mission 1: Date Calculator Template #
#######################################

#############################
# Task 1 - Helper Functions #
#############################

###########
# Task 1a #
###########
def is_leap_year (year):
    """
    is_leap_year (year) -> boolean
    Function takes in a specific year.
    Returns True if it is a leap year, False otherwise.
    """
    ## Your Code Here ##
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    return False

# print("Leap year: ")  
# print (f"2000: {is_leap_year(2000)}") # True
# print (f"1900: {is_leap_year(1900)}") # False
# print (f"1984: {is_leap_year(1984)}") # True
# print (f"2015: {is_leap_year(2015)}") # False
# print("-" * 20)

###########
# Task 1b #
###########
def days_in_month (month , leap = False):
    """
    days_in_month (month) -> int
    Function takes in a specific month.
    Returns number of days in that month for a normal year.
    
    Note: This function needs not to consider leap year.
    """
    ## Your Code Here ##
    ## Your Code Here ##
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    
    if month == 2:
        return 29 if leap else 28
    
    if month in (4, 6, 9, 11):
        return 30

##Print out number of days in each month:
# print("number of days in each month:")
# for i in range (1, 13):
#     print (i, days_in_month(i))
# print("-" * 20)

###########
# Task 1c #
###########
def num_of_leap_years (start_year, end_year):
    """
    num_of_leap_years (start_year, end_year) -> int
    Function takes in 2 years: start_year (inclusive) and end_year (exclusive).
    Returns number of leap years in between the 2 years.
    """
    ## Define num_of_leap_years using iterative loop ##
    ## Your Code Here ##
    total_leap_year = 0
    
    for i in range(start_year, end_year):
        
        if is_leap_year(i):
            
            total_leap_year += 1
        
    return total_leap_year

# print("num of leap years")
# print (f"between 2010 and 2016: {num_of_leap_years(2010, 2016)}") # 1
# print (f"between 2008 and 2013: {num_of_leap_years(2008, 2013)}") # 2
# print (f"between 1900 and 2016: {num_of_leap_years(1900, 2016)}") # 28
# print("-" * 20)

###########
# Task 1d #
###########
def is_valid_date (date):
    """
    is_valid_date (date) -> boolean
    Function checks if the date entered is a valid date.
    Returns True if it's valid, False otherwise.
    """
    ## Your Code Here ##
    try:
        day = int(date[:2])
        month = int(date[2:4])
        year = int(date[4:])

        if year < 1900:
            return False

        if month > 12:
            return False

        max_days = int(days_in_month(month, is_leap_year(year)))
        
        return (day <= max_days)

    except:
        return False

# print("is valid date")
# print (f'29022016: {is_valid_date("29022016")}') # True
# print (f'31042015: {is_valid_date("31042015")}') # False
# print (f'29022015: {is_valid_date("29022015")}') # False
# print("-" * 20)

###########################
# Task 2 - Main Functions #
###########################

###########
# Task 2a #
###########
def num_of_days_from_1900 (date):
    """
    num_of_days_from_1900 (date) -> int
    Function takes in a date.
    Returns the number of days of the input date after "01011900".
    """
    ## Your Code Here ##
    if not is_valid_date(date):
        return False

    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    total_days = day

    for i in range(1, month):
        total_days += days_in_month(i, is_leap_year(year))
    
    for i in range(1900, year):
        total_days += 365 if not is_leap_year(i) else 366

    return total_days - 1

# print("num of days from 1900")
# print (f'30011900: {num_of_days_from_1900("30011900")}') # 29
# print (f'28021900: {num_of_days_from_1900("28021900")}') # 58
# print (f'01031904: {num_of_days_from_1900("01031904")}') # 1520
# print (f'31012016: {num_of_days_from_1900("31012016")}') # 42398
# print("-" * 20)

###########
# Task 2b #
###########
def days_between_2_dates (date1, date2):
    """
    days_between_2_dates (date1, date2) -> int
    Function takes in 2 dates.
    Returns the number of days in between the 2 dates.
    """
    ## Your Code Here ##
    if not is_valid_date(date1) or not is_valid_date(date2):
        return False

    return abs(num_of_days_from_1900(date1) - num_of_days_from_1900(date2))

# print("days between two dates")
# print (f'between 15041984 and 26102000: {days_between_2_dates("15041984", "26102000")}') # 6038
# print (f'between 26102000 and 15041984: {days_between_2_dates("26102000", "15041984")}') # 6038
# print (f'between 26102000 and 31012016: {days_between_2_dates("26102000", "31012016")}') # 5575
# print("-" * 20)

###########
# Task 2c #
###########
def offset(date, offset_days):

    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    if offset_days == 0:
        return date
    
    d_in_month = days_in_month(month, is_leap_year(year))

    if offset_days + day <= d_in_month:
        return (offset_days + day, month, year)

    offset_days += day

    while True:
        d_in_month = days_in_month(month, is_leap_year(year))

        if offset_days > d_in_month:
            offset_days -= d_in_month
            month += 1
            if month > 12:
                month = 1
                year += 1

        else:
            break

    return (offset_days, month, year)
        

def add_n_days_after_1900 (days):
    """
    add_n_days_after_1900 (days) -> date
    Function takes in a specific number of days.
    Returns the date after adding the input number of days to "01011900".
    """
    ## Your Code Here ##
    day, month, year = offset("01011900", days)
    return f"{str(day).zfill(2)}{str(month).zfill(2)}{year}"



# print("add n days after 1900")
# print (f'30: {add_n_days_after_1900(30)}') # "31011900"
# print (f'31: {add_n_days_after_1900(31)}') # "01021900"
# print (f'59: {add_n_days_after_1900(59)}') # "01031900"
# print (f'1519: {add_n_days_after_1900(1519)}') # "29021904"
# print (f'1520: {add_n_days_after_1900(1520)}') # "01031904"
# print("-" * 20)

###########
# Task 2d #
###########
def add_n_days_from_a_date (date, days):
    """
    add_n_days_from_a_date (date, days) -> date
    Function takes in a date and a specific number of days.
    Returns the date after adding the input number of days to the input date.
    """
    ## Your Code Here ##
    if not is_valid_date(date):
        return False
    day, month, year = offset(date, days)
    return f"{str(day).zfill(2)}{str(month).zfill(2)}{year}"

# print("add n days from a date")
# print (f'date is 15041984 and n is 6038 {add_n_days_from_a_date ("15041984", 6038)}') # 26102000
# print (f'date is 26102000 and n is 6038 {add_n_days_from_a_date ("26102000", 6038)}') # 08052017
# print("-" * 20)

###########
# Task 2e #
###########
def weekday_of_date (date):
    """
    weekday_of_date (date) -> str
    Function takes in a date.
    Returns the weekday of the input date.
    """
    ## Your Code Here ##
    if not is_valid_date(date):
        return False
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][num_of_days_from_1900(date) % 7]

# print("weekday of date")
# print (f'01011900 {weekday_of_date("01011900")}') # "Monday"
# print (f'02011900 {weekday_of_date("02011900")}') # "Tuesday"
# print (f'3101201 {weekday_of_date("31012016")}') # "Sunday"
# print("-" * 20)

############################
# Task 3 - Date Calculator #
############################
def date_calculator():
    """
    date_calculator ()
    Function takes in an input from user and performs the functions accordingly.
    """
    done = False
    while not done:
        # Prepare Menu
        print ("-----------------------------------------")
        print ("Welcome to date calculator")
        print ("  1. Calculate number of days between 2 dates.")
        print ("  2. Add n days from a date.")
        print ("  3. Find weekday of a date.")
        print ("  4. Exit the programme.\n")
        print ("**Please note the format of date should follow the format of 'DDMMYYYY'\n")
        
        # Get Input
        option = int(input ("Select a function: "))
        
        ## Your Code Here ##
        if option == 1:
            date1 = str(input("Enter first date: "))
            while not is_valid_date(date1):
                date1 = str(input("Please enter a valid first date: "))

            date2 = str(input("Enter second date: "))
            while not is_valid_date(date2):
                date2 = str(input("Please enter a valid second date: "))

            print(days_between_2_dates(date1, date2))
            
        elif option == 2:
            date = str(input("Enter date: "))
            while not is_valid_date(date):
                date = str(input("Please enter a valid date: "))
            
            while True:
                n = input("Enter offset: ")
                try:
                    n = int(n)
                    if n >= 0:
                        break
                    else:
                        print("Please enter a valid integer")

                except:
                    print("Please enter a valid integer")
            
            print(add_n_days_from_a_date(date, n))

        elif option == 3:
            date = str(input("Enter date: "))
            while not is_valid_date(date):
                date = str(input("Please enter a valid date: "))
            
            print(weekday_of_date(date))

        elif option == 4:
            done = True
        
        else:
            print("Please enter a valid option")


#date_calculator()