bookspaid = int(input("How many books did you purchase this month?: "))

if bookspaid == 0:
    points = 0
elif bookspaid == 2:
    points = 5
elif bookspaid == 4:
    points = 15
elif bookspaid == 6:
    points = 30
else:
    points = 60
print("You have points awarded: ", points)