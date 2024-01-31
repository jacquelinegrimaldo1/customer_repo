import csv

file_object = open('Employee_data.csv', 'r')
csv_file = csv.reader(file_object)
next(csv_file)

for rec in csv_file:
    name = rec[1]
    salary = float(rec[3])
    bonus = float(rec[7])
    bonus_calc= salary * (bonus)
    total_pay = salary * (1 + bonus)
    
    print(f'Name: {name}\n Salary: $ {salary:,.2f}\n Bonus: $ {bonus_calc:,.2f}\n Pay: $ {total_pay:,.2f}\n')

file_object.close()