
import csv
file_object= open('customers.csv', 'r')
csv_file= csv.reader(file_object)
next(csv_file)
outfile= open('customer_country.csv', 'w')
outfile.write('Full name, Country\n')
for rec in csv_file: 
    outfile.write(f"{rec[1]} {rec[2]}, {rec[4]}\n")
outfile.close()
                  


