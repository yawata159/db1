import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

for k in d:
    print k['name'] + ", " + k['id']
    #Q: What can you print here to make each line show only
    #   a name and its ID?
    #   eg,
    #   sasha, 3

    
