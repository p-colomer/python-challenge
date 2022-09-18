import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
file_txt  = os.path.join("Analysis", "output.txt")



with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    monthcount = 0
    net_total = 0
    changes = 0
    difference = 0
    current = 0
    previous = 0

    line_count = 0
    greatest_increase = 0
    greatest_decrease = 0
    for row in csvreader:
        
        monthcount += 1
        net_total = net_total + int(row[1])

        if line_count == 0:

            previous = float(row[1])
            line_count += 1
        else:
        
            current = float(row[1])
            difference = current - previous
            if difference > greatest_increase:
                greatest_increase = difference
                greatest_increase_date = row[0]
            
            if difference < greatest_decrease:
                greatest_decrease = difference
                greatest_decrease_date = row[0]
            changes = changes + difference
            difference = 0
            previous = current


total_changes = changes / (monthcount - 1)

with open(file_txt,"w") as f:
    print("\nFinancial Analysis \n----------------------------------------", file = f)
    print("\nTotal months: " , monthcount, file = f)
    print("\nTotal: $" +  str(round(net_total)), file = f)
    print("\nAverage change: $" + str(round(total_changes,2)), file = f)
    print("\nGreatest Increase in Profits: " + greatest_increase_date + " ($"+ str(round(greatest_increase))+")", file = f)
    print("\nGreatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(round(greatest_decrease))+")", file = f)
    print("\nFinancial Analysis \n----------------------------------------")
    print("\nTotal months: " , monthcount)
    print("\nTotal: $" +  str(round(net_total)))
    print("\nAverage change: $" + str(round(total_changes,2)))
    print("\nGreatest Increase in Profits: " + greatest_increase_date + " ($"+ str(round(greatest_increase))+")")
    print("\nGreatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(round(greatest_decrease))+")")



