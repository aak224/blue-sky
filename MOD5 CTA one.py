years = int(input("How many years in the study?: "))

total = 0
for x in range(years):     
    # Inner loop: Iterate from 1 to 12 months
    for months in range(1, 13):
        rainmonthly = int(input("How many inches of rain this month?  "))
        total += rainmonthly

print(years * 12 )
print(total)
print(total/(years*12))