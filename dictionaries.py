"""books = {'jalal': 'The Kite Runner',
         'khaled': 'A Thousand Splendid Suns',
         'dan': 'Digital Fortress'}
print(f"The book {books['jalal']} is written by Jalal.")"""

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
