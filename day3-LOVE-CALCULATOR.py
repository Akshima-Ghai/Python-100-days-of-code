#LOVE CALCULATOR
print("Welcome to LOVE CALCULATOR")
name = input("Enter your name ").lower()
crush_name = input("Enter your crush name ").lower()
# name_lower = name.lower()
# crush_name_lower = crush_name.lower()
t = name.count('t') + crush_name.count('t')
r = name.count('r') + crush_name.count('r')
u = name.count('u') + crush_name.count('u')
e = name.count('e') + crush_name.count('e')

l = name.count('l') + crush_name.count('l')
o = name.count('o') + crush_name.count('o')
v = name.count('v') + crush_name.count('v')

first_digit = t+r+u+e
last_digit = l+o+v+e
percent = str(first_digit)+str(last_digit)
print(f"you are {percent} percent compatible with your crush\n")

