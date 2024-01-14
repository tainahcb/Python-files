adjective ='clever'
animal ='monkey'
verb ='jump'
exclamation ='Woow'
verb1 = 'shout'
verb2 = 'run'

print(f'The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb} down the hallway. \"{exclamation}\"! I yelled. But all')
print(f'I could think to do was to {verb1} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb2}')
print(f'right in front of my family.')


#The use of the "input" function in this text to replace start data:

adjective = input('Choose an adjective:').capitalize()
animal = input('Choose an animal:').capitalize()
verb = input('Choose your first verb:').capitalize()
exclamation = input('What is your exclamation?').capitalize()
verb1 = input('Please, choose a second verb:').capitalize()
verb2 = input(' Please, choose a trird verb:').capitalize()

print(f'The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb} down the hallway. \"{exclamation}\"! I yelled. But all')
print(f'I could think to do was to {verb1} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb2}')
print(f'right in front of my family.')