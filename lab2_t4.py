# S.L. Broschat
# CptS 111
# Lab #2, Task 4
#
# Code to calculate the number of quarters, dimes, nickels, and pennies in
# a given number of cents.

# Prompt user for number of cents:
print()
cents = int(input('Enter the number of cents: '))
print()

# Calculate the number of quarters, dimes, nickels, and pennies, and
# print results.
quarters, rem_cents = divmod(cents, 25)
dimes, rem_cents = divmod(rem_cents, 10)
nickels, pennies = divmod(rem_cents, 5)
print(f'There are {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s),\
 and {pennies} pennies in {cents:,} cents.')

