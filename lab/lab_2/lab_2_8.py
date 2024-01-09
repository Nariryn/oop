def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def day_of_year(day, month, year):
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        day_in_month[1] = 29
    return sum(day_in_month[:month-1]) + day # yearStart posirion - > 12 // yearend 1 -> position 

def day_in_year(year):
  if(is_leap(year)):
    return 366
  return 365

def date_diff(date1, date2):
    date1 = list(map(int, date1.split("-")))
    date2 = list(map(int, date2.split("-")))
    diff_date = 0
    for year in range(date1[2], date2[2]): # date1[2] - 1
        diff_date += day_in_year(year)  
    diff_date += (day_of_year(date2[0], date2[1], date2[2]) - day_of_year(date1[0], date1[1], date1[2])) + 1
    
    return diff_date

date1 = input("Enter the first date [DD-MM-YYYY]: ")
date2 = input("Enter the second date [DD-MM-YYYY]: ")

result = date_diff(date1, date2)
print(f"difference days is: {result} days.")