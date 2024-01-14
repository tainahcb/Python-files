"""
Author: Tainah Correia Barreto
"""

print('Please enter the following information: ')
first=input('First name:')
last=input('Last name:')
email=input('Email address:')
phone=input('Phone number:')
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()

print(f"Hair: {hair_color:12} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------")
print()

#Structure made without input

first_name = 'Tainah'
last_name = 'Barreto'
email_adress ='tainah.s.correia@gmail.com'
phone_number = '+55 79 9 98513488'
job_title ='Software Engineer'
id_number ='157556'
hair ='brown'
eyes ='brown'
month ='june'
training ='yes'

print('Structure made without input:')
print()
print('first name:'.capitalize()+first_name)
print('last name:'.capitalize()+last_name)
print('email address:'.capitalize()+email_adress)
print('phone number:'.capitalize()+phone_number)
print('job title:'.capitalize()+job_title)
print('id '.upper()+ 'number:'.capitalize()+id_number)
print()
print('The'.capitalize()+' ID'.upper()+' card'.capitalize()+' is')
print('--------------------------------------')
print(last_name.capitalize()+","+ first_name.capitalize())
print(job_title)
print('id:'.capitalize()+ id_number)
print()
print(email_adress)
print(phone_number)
print('--------------------------------------')