import csv
from datetime import date
today=date.today()
x=today.strftime("%d-%m-%Y")
#gives current time
employees=[]
salary=float(input("enter your income"))
def tax_func(salary)->float:
    #income tax calculator
    if salary<=12570:
        tax=0
        #personal allowance 12,570 0%
        #no tax if salary is less than/equal to 12570
    elif salary<=50270:
        tax=(salary-12570)*0.2
        #basic rate 12,571 to 50,270 20%
    elif salary<=150000:
        #higher rate 50,270 to 150,000 40%
        tax=(50270-12570)*0.2
        tax+=(salary-50270)*0.4
    elif salary>150000:
        #additional rate over £150,000 45%
        tax=(50270-12570)*0.2
        tax+=(150000-50270-12570)*0.4
        tax+=(salary-150000)*0.45
    return tax
def student_financer(salary)->float:
    #calculate student payment, salary-student threshold x 9%
    return(salary-(2274*12))*0.09
def national_insurance(salary)->float:
    #national insurance calculator
    lower=1048.01*12
    higher=4189*12
    if salary<=lower:
        ni=0
    elif salary<=higher:
        ni=(salary-lower)*0.12
    elif salary>higher:
        ni_lower=(higher-lower)*0.12
        ni_higher=(salary-higher)*0.2
        ni=ni_lower+ni_higher
    return ni
def pension(salary)->float:
    #pension calculator
    if salary>=84193.99:
        p=salary*0.117
    elif salary>=61742.99:
        p=salary*0.113
    elif salary>=46586.99:
        p=salary*0.102
    elif salary>=39290.99:
        p=salary*0.096
    elif salary>=29187.99:
        p=salary*0.086
    else:
        p=salary*0.074
    return p
tax=tax_func(salary)
sp=student_financer(salary)
ni=national_insurance(salary)
p=pension(salary)
#calls all functions to place it together in payslip module
def payslip(salary, tax, national_insurance, student_payment, pension,name):
    file_name=str(x)
    file_name=file_name+"_"+name
    print(file_name)
    #creates file with date created and employee name, and prints it 
    file=open(file_name+".txt","w")
    file.write("Name:            \t"+ name)
    file.write("salary:          \t"+("{:.2f}".format(salary)))
    file.write("tax:             \t"+("{:.2f}".format(tax)))
    file.write("national insurance tax:\t"+("{:.2f}".format(national_insurance)))
    file.write("pension contribution:\t"+("{:.2f}".format(pension)))
    file.write("student payment tax:\t"+("{:.2f}".format(student_payment)))
    #writes to file, the tax details 
    taxed_salary=salary-(tax+student_payment+national_insurance+pension)
    dp=("{:.2f}".format(taxed_salary))
    #calculates salary after tax and places it into 2dp format 
    filewrite="salary after tax:  \t"+ dp+"\n"
    file.write(filewrite)
def database_create():
    #initial function to create employee database csv file 
    salary=[["Watts",45000],["Conner",1000],["Virk",30000],["Macdonald",15000]]
    file=open("employee_database.csv","w", newline="")
    csv_writer=csv.writer(file)
    for i in salary:
        csv_writer.writerow(i)
    file.close()
def database_read():
    #function to read database of employees 
    employees=[]
    file=open("employee_database.csv","r")
    file_reader=csv.reader(file)
    for row in file_reader:
        employees.append(row)
    file.close()
    print(employees)
    return employees
    #returns array of employees from csv file
def payslip_spawn(employees):
    for i in employees:
        print(i)
        name=i[0]
        salary=i[1]
        salary=int(salary)
        payslip(salary, tax, ni, sp, p,name)
        #displays payslip
        
employees=database_read()
#calls function to create employees array to use it in payslip_spawn
payslip_spawn(employees)

