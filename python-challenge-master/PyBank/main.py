
import os

import csv

csvpath = os.path.join( '','Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    i =0
    total =0
    #print(csvreader)

    csv_header = next(csvreader)
    month = []
    amount = []
    monthlychange = []
    greatestincrease = 0
    greatestdecrease = 0
    maxincreasemonth = ""
    maxdecreasemonth = ""
    averagechange = 0
    for row in csvreader:
        i += 1
        total += int(row[1])
        month.append(row[0])
        amount.append(row[1])
    for j in range(i-1):
        monthlychange.append(int(amount[j+1])-int(amount[j]))
    greatestdecrease = min(monthlychange)
    greatestincrease = max(monthlychange)
    maxdecreasemonth = month[(monthlychange.index(greatestdecrease))+1]
    maxincreasemonth = month[monthlychange.index(greatestincrease)+1]
    averagechange = round(sum(monthlychange)/len(monthlychange),2)
   

print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(i))
print("Total : $"+str(total))
print("Average Change : $"+str(averagechange))
print("Greatest increase in Profits : "+maxincreasemonth+ " " + "( $"+str(greatestincrease)+ ")")
print("Greatest decrease in Profits : "+maxdecreasemonth+ " " + "( $"+str(greatestdecrease)+ ")")

output = os.path.join('','analysis', 'pybank_output.txt')
with open(output, 'w') as csvfile:
    csvfile.truncate()
    csvfile.write("Financial Analysis \n")
    csvfile.write("--------------------")
    csvfile.write("\n")
    csvfile.write("Total Months: " + str(i))
    csvfile.write("\n")
    csvfile.write("Total : $"+str(total))
    csvfile.write("\n")
    csvfile.write("Average Change : $"+str(averagechange))
    csvfile.write("\n")
    csvfile.write("Greatest increase in Profits : "+maxincreasemonth+ " " + "( $"+str(greatestincrease)+ ")")
    csvfile.write("\n")
    csvfile.write("Greatest decrease in Profits : "+maxdecreasemonth+ " " + "( $"+str(greatestdecrease)+ ")")
    csvfile.write("\n")
    csvfile.close()