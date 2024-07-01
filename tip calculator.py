print("Welcome to tip calculator.")
total=float(input("What was the total bill? "))
tipper=int(input("What percentage tip would you like to give? "))
ppl=int(input("How many people present to split the bill? "))

tip = total * tipper / 100
total+=tip
eachper=total / ppl
print("Each person has to pay",round(eachper,2))