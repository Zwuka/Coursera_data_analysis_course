import csv
table = {}
list1 = []
with open("hight.csv",newline='') as file:
    csvf = csv.DictReader(file)
    for row in csvf:
        table[row['City']] = row
    list1 = csvf.fieldnames    

print(list1)
print (table)

for key in table:
    print (table[key])

#for key,value in table.items():
    #print (key)
    #print (value)
#    for value1 in value:
#    print(value1,type(value1))


with open("test3.csv",'w',newline = '') as file:
    csvf = csv.DictWriter(file,list1)
    csvf.writeheader()
    for key in table:
        csvf.writerow(table[key])
    