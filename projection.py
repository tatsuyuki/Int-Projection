import datetime
from datetime import date
from datetime import timedelta
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
import os.path




### File path is temporary, to be updated on final version

### To declare a class for function reusability

if os.path.isfile("/Users/Michael/Documents/GitHub/Int-Projection/projection.csv") == False:   #Check if table file exist



    head = ['Dealer', 'Loan No.', 'Name', 'Details', 'Amount', 'Interest', 'Agreement Date', 'Tenure'] 

    with open('/Users/Michael/Documents/GitHub/Int-Projection/projection.csv', 'w') as a:   ###Create file and write header row if file 
        writer = csv.writer(a)                                                   ###does not exist
        writer.writerow(head)
else:
    print ("File exist, entering appending mode")   #Message if file exist


def write_func():            ###Get input from user and append to table file
    
    dbase = []

    dealer = raw_input("Dealer:  ")
    hirer = raw_input("Hirer's Name:  ")
    acNum = raw_input("Loan Number:   ")
    details = raw_input("Loan Details:  ")
    agg_date = str(raw_input("Agreement Date (yyyymmdd):"))
    ###     While loop to ensure correct date format for ease of processing
    while len(agg_date) != 8:
        agg_date = str(raw_input("Invalid Date Format! Try again (yyyymmdd):"))
        
    format_date = agg_date[6:8] + '-' + agg_date[4:6] + '-' + agg_date[0:4]  #format for human eye
    amount = input("Loan Amount:   ")
    interest = input("Loan Interest:  %")
    tenure = input("No of Months: ")


    dbase = [dealer, acNum, hirer, details, amount, interest, format_date, tenure]

    with open('/Users/Michael/Documents/GitHub/Int-Projection/projection.csv', 'a') as b:
        writer = csv.writer(b)
        writer.writerow(dbase)
        
def read_func():            ###Print out table file
    with open('/Users/Michael/Documents/GitHub/Int-Projection/projection.csv', 'r') as c:
        reader = csv.reader(c)
        for row in reader:
            print row

def dict_read():                        
    data_in = csv.DictReader(open("/Users/Michael/Documents/GitHub/Int-Projection/projection.csv"))

    for r in data_in:
        print r

def hp_interest(tenure, interest, amount):                                  ### Calculate HP interest given the param
    term_charge = float(amount * float(tenure/12)) * float(interest)/100 #Getting term charge
    ###print term_charge
    int_constant = float(((tenure)*(tenure+1))/2) #Calculating interest constant for use in formula 
    ###print int_constant                           *skipping full formula for simplicity
    instalment = tenure
    ###print instalment
    interest_tab = []
    count = 0
    count_tab = []
    while instalment > 0:
        interest = float(((instalment) / (int_constant)) * (term_charge))
        interest_tab.append(interest)
        count += 1
        instalment -= 1
        count_tab.append(count)

    ###for i in interest_tab:
    ###    print i
    ###for i in count_tab:
    ###    print i
    return interest_tab

def agreement_date(string):                 ###convert a set of string into date

    ag_date = datetime.strptime(str(string), '%Y%m%d')
   
    return ag_date





agreement_date(20120310)

begin = raw_input("Write or Read?")
if (begin == "Write") or (begin == "write"):
    write_func()
    validinput = True
    
elif (begin == "Read") or (begin == "read"):
    read_func()
    validinput = True

else:
    validinput = False
    
while validinput == False:
    print ("Wrong input, please try again")
    begin = raw_input("Write or Read?")
    if begin == 'Write' or begin == 'write':
        write_func()
        validinput = True

    elif begin == 'Read' or begin == 'read':
        read_func()
        validinput = True


            



    
