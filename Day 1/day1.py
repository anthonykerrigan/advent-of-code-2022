import csv

class importInput:
    elf = 0
    with open('Calories.csv', newline='') as csvfile: 
        elflist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in elflist:
            if row in (None, "",[]):
                elf += 1
                print("elf "+str(elf))