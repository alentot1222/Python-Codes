#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

# Prompt user for input and convert to appropriate data types
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))

# Compute tip amount based on user input
percent_1 = 10 / 100  # no need to use int() here since 10 is already an integer
percent_2 = 12 / 100
percent_3 = 15 / 100

if percent == 10:
    tip_percent = percent_1
elif percent == 12:
    tip_percent = percent_2
elif percent == 15:
    tip_percent = percent_3
else:
    print("Invalid percent value.")
    tip_percent = None

# Compute amount to be paid by each person
if tip_percent is not None:
    total_bill = bill + (bill * tip_percent)
    split = total_bill / persons
    print("Each person should pay: ${:.2f}".format(split)) # round the split to 2 decimal places
