"""books = {'jalal': 'The Kite Runner',
         'khaled': 'A Thousand Splendid Suns',
         'dan': 'Digital Fortress'}
print(f"The book {books['jalal']} is written by Jalal.")

alien = {'x_position': 0, 'y_position': 25}
print(f"Original position: {alien['x_position']}")

alien['speed'] = input("Enter the speed of the alien: ")

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien['x_position'] += x_increment
print(f"New position: {alien['x_position']}")

print(alien)
del alien['speed']
print(alien)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

lang = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {lang}.")
"""

glossary = {
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list.',
    'if statement': 'A statement that checks a condition.',
    'loop': 'Work through a collection of items, one at a time.',
}

for i,j in glossary.items():
    print(f"{i.title()}: \n\t{j.title()}")