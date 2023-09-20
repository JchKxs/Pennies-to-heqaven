num_of_pennies = input("Please enter the number of your pennies: ")
num_of_pennies = int(num_of_pennies)

p_in_dollar = 100
p_in_quarter = 25
p_in_dime = 10
p_in_nickel = 5

num_of_dollars = num_of_pennies // p_in_dollar
print(f"Dollars: {num_of_dollars}")

the_change = num_of_pennies % p_in_dollar

num_of_quarters = the_change // p_in_quarter 
print(f"Quarters: {num_of_quarters}")

the_change = the_change % p_in_quarter

num_of_dimes = the_change // p_in_dime
print(f"Dimes: {num_of_dimes}")

the_change = the_change % p_in_dime 

num_of_nickels = the_change // p_in_nickel
print(f"Nickels: {num_of_nickels}")

the_change = the_change % p_in_nickel

print(f"Pennies: {the_change}")