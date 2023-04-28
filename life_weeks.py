# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


age = input("What is your current age? ")
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
