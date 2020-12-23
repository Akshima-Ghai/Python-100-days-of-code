# WHO'S PAYING BILLS
# import random
#
# names = input("Enter names seperated by comma. ")
# name_list = names.split(",")
# n = len(name_list)
# index = random.randint(0, n - 1)
# print(f"{name_list[index]} will pay the bill")

# OR

import random
names = input("Enter name seperated by comma. ")
name_list = names.split(",")
person_who_will_pay_bill = random.choice(name_list)
print(f"{person_who_will_pay_bill} will pay the bill")
