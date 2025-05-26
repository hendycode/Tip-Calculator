print("Welcome to the the tip calculator!")
totalbill = int(input("What was the total bill? "))
tiptotal = totalbill * (int(input("How much tip would you like to give? (%) ")) / 100)
nopeeps = int(input("How many people will split the bill? "))

perbill = totalbill / nopeeps
pertip = tiptotal / nopeeps
total = perbill + pertip
print(f"Alright, so each person will pay Ksh{total}, thank you for visting us")