"""
Author= Tainah Correia Barreto
Project 02: Meal Price Calculator
"""
#This project has variables and formats that include: float, replace, input .
#With formatting tips and functional shortcuts.

# Collecting Information
picec=float(input("What is the price of child's meal?"))
numberc=int(input("What is the number of child's meal?"))
picea=float(input("What is the price of adult's meal?"))
numbera=int(input("What is the number of adult's meal?"))

print()

# Calculating the meal subtotal : adults and children
# Another way to format the currency symbol is valor_usd ='\u0024'

subtotala=float(picea*numbera)
subtotalc=float(picec*numberc)
subtotal=float(subtotala)+float(subtotalc)
valor_usd="${:,.2f}".format(subtotal).replace(",", "X").replace(".", ",").replace("X", ".")

print(f"Subtotal children:{subtotalc:.2f}")
print(f"Subtotal adults:{subtotala:.2f}")
print(f"Subtotal of meal for adult and child is:{valor_usd}")
print()


#Calculating the tax rate
tax=float(input("What is the sales tax rate?"))
c_tax=(subtotal*tax)/100
c_total=(subtotal+c_tax)
sc_tax="${:,.2f}".format(c_tax).replace(",", "X").replace(".", ",").replace("X", ".")
sc_total="${:,.2f}".format(c_total).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'Sales Tax:{sc_tax}')
print(f"Total:{sc_total}")
print()

#Calculating the payment
pay=float(input("What is the payment amount?"))
subtraction=pay-c_total
s_dif= "${:,.2f}".format(subtraction).replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Change:{s_dif}")
print()

print(f"Have a great meal!")

