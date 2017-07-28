'''Write a program that indicates whether a specified month has 28, 30, or 31 days.'''

#(hint: something goes here)

def numDays(month):
    January == "31"
    February == "28"
    March == "31"
    April == "30"
    May == "31"
    June == "30"
    July == "31"
    August == "31"
    September == "30"
    October == "31"
    November == "30"
    December == "31"
    if(month == "January") or (month == "March") or (month == "May") or (month == "July") or (month == "August") or (month == "October") or (month == "December"):
        return "31"
    elif(month == "April") or (month == "June") or (month == "September") or (month == "November"):
        return "30"
    elif(month == "February"):
        return "28"







def main():
    days = numDays(September)
    print(days)

main()
