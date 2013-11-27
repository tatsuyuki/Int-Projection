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

if os.path.isfile("/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv") == False:   #Check if table file exist



    head = ['Loan No.', 'Agreement Date']
    ins = 0
    while ins < 300:
        ins += 1
        head.append(ins)

    with open('/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv', 'w') as a:   ###Create file and write header row if file 
        writer = csv.writer(a)                                                   ###does not exist
        writer.writerow(head)
else:
    print ("File exist, entering appending mode")   #Message if file exist



##### Class for Code Reusability

class inc_project(object):

    def __init__(self):
        pass
        







"""def write_func():            ###Get input from user and append to table file
    
    dbase = []

    dealer = raw_input("Dealer:  ")
    hirer = raw_input("Hirer's Name:  ")
    ###     acNum to test for duplicate number
    acNum = raw_input("Loan Number:   ")
    with open('/Users/Michael/Documents/GitHub/Int-Projection/projection.csv', 'r') as compare:
        reader = csv.reader(compare)
        for row in reader:
            if str(row) == str(acNum):
                acNum = raw_input("Duplicate Loan No! Recheck and try again!")
                    
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
"""
        
""" hp_interest to be modified to take 1 param, loan-number and match it against table in projection.csv for the
    respective loan.
    and subsequently the required details to calculate the interest
"""
def hp_interest(tenure, tc, l_no, agg_date):                                  ### Calculate HP interest given the param
    #term_charge = float(amount * float(tenure/12)) * float(interest)/100 #Getting term charge
    ###print term_charge
    int_constant = float(((tenure)*(tenure+1))/2) #Calculating interest constant for use in formula 
    ###print int_constant                           *skipping full formula for simplicity
    instalment = tenure
    ###print instalment
    term_charge = tc
    
    format_date = agg_date[6:8] + '-' + agg_date[4:6] + '-' + agg_date[0:4]  #format for human eye
    interest_tab = [str(l_no), str(format_date)]
    count = 0
    count_tab = ['Loan Number']
    while instalment > 0:
        interest = float(((instalment) / (int_constant)) * (term_charge))
        interest_tab.append(interest)
        count += 1
        instalment -= 1
        count_tab.append(count)

    """hp_header = count_tab
    with open('/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv', 'w') as h:
        writer = csv.writer(h)
        writer.writerow(hp_header)"""

    with open('/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv', 'a') as ins:
        writer = csv.writer(ins)
        writer.writerow(interest_tab)
    
    

    ###for i in interest_tab:
    ###    print i
    ###for i in count_tab:
    ###    print i
    return interest_tab

def agreement_date(string):                 ###convert a set of string into date

    ag_date = datetime.strptime(str(string), '%Y%m%d')
   
    return ag_date

##generate list of 12 months and populate relavant interest

def calendar(string):

    c.header = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return





"""begin = raw_input("Write or Read?")
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

"""

cont = True
proceed = raw_input("Continue?")
if proceed == 'Yes' or proceed == 'yes' or proceed == 'y':
    cont == True
    while cont == True:
        l_num = str(raw_input("Loan Number:  "))
        f_lnum = l_num[0:2] + '/' + l_num[2:5]
        tenure = input("Tenure(months): ")
        interest = input("Term Charge: ")
        #amt = input("Loan Amount: ")
        agg_date = str(raw_input("Agreement Date (yyyymmdd):"))
    ###     While loop to ensure correct date format for ease of processing
        while len(agg_date) != 8:
            agg_date = str(raw_input("Invalid Date Format! Try again (yyyymmdd):"))

        hp_interest(tenure, interest, f_lnum, agg_date)
        cont1 = raw_input("Do you want to continue?")
        if cont1 != 'NO' or cont1 != 'no' or cont1 != 'n':
            cont = True

        else:
            cont = False
else:
    print "Program Ended. Terminated by user"



    
