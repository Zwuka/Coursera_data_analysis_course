
with open("test2.csv",'w',newline = '') as file:
    csvf = csv.DictWriter(file,list1)
    csvf.writeheader()
    for key in dict_2:
        csvf.writerow(dict_2[key])