# WHO'S PAYING BILLS
import random

names = input("Enter names seperated by comma. ")
name_list = names.split(",")
n = len(name_list)
index = random.randint(0, n - 1)
print(f"{name_list[index]} will pay the bill")
