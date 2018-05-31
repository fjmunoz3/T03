import csv

with open('genres.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    i=0
    for row in spamreader:
        row = row[0].split(",")
        #print(', '.join(row))
        #print(type(row[0]))
        print(row[0], row[1])
        i += 1
        if i == 20:
            break
    
