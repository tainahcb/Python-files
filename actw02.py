"""
Author: Tainah Correia Barreto
PC1 103 - Introduction to Programming
W02 Prepare Learning Activities

"""

#The aim of this activity is to collect data and convert it into numbers to fill in the form.
print("Welcome to date planner!\nYou need to fill in the form below: ")
print()

age_form=input('How old are you?')
age=int(age_form)
total=age+1
print(f'On you next birthday, you will be {total}')
print()

#I chose to use str as the second option for number conversion.
egg_carton=input('How many egg cartons do you have?')
carton=str(egg_carton)
total=int(egg_carton)*int(12)
print(f'You have {total} eggs')
print()

#Use of strings: float, str and input with the format string(print(f')).
cookies=input('How many cookies do you have?')
people=input('How may people are there?')
cookie=str(cookies)
person=str(people)
total=float(cookie)/float(person)
print(f'Each person may have {total} cookies')
print()
print("Thanks for your help!")