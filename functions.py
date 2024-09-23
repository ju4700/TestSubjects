#import guests
#from guests import inv

"""alines = []

for i in range(30):
    new_a = {'color': 'red', 'x': 0, 'y': 0, 'speed': 1}
    alines.append(new_a)

for aline in alines[:3]:
    print(aline)

pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)