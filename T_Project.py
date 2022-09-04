# calculater
# ----------

title = "calculater"

print(title.upper())
print("----------")

num_1 = float(input("Ender your first number: "))
num_2 = float(input("Ender your second number: "))
print()
op = input("Ender your oprator [+, -, /, *]: ")
print()

if op == '+':
    out = num_1 + num_2 
    print(f"The {num_1} + {num_2} is {out}\n")
elif op == '-':
    out = num_1 - num_2
    print(f"The {num_1} - {num_2} is {out}\n")
elif op == '/':
    out = num_1 / num_2
    print(f"The {num_1} / {num_2} is {out}\n")
elif op == '*':
    out = num_1 * num_2
    print("The {num_1} + {num_2} is {out}\n")
else:
    print("You typed an invalid oprator, please try agin.\n")