# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
A = int(age)
days1 = A * 365
weeks1 = A * 52
months1 = A * 12
B = int(90)
days2 = B * 365
weeks2 = B * 52
months2 = B * 12

fdays = days2 - days1
fweeks = weeks2 - weeks1
fmonths = months2 - months1

print(f"You have {fdays} days, {fweeks} weeks, and {fmonths} months left.")