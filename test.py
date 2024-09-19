bycycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycycles) # ['trek', 'cannondale', 'redline', 'specialized']
print(bycycles[0]) # trek

massage = f"My first Cycle was {bycycles[0].title()}."
print(massage) # My first Cycle was Trek.

bycycles[0] = 'honda'
print(bycycles) # ['honda', 'cannondale', 'redline', 'specialized']

bycycles.append('ducati')
bycycles.insert(0, 'bmw')
print(bycycles) # ['bmw', 'honda', 'cannondale', 'redline', 'specialized', 'ducati']

del bycycles[1]
print(bycycles) # ['bmw', 'cannondale', 'redline', 'specialized', 'ducati']

bycycles.insert(2, 'honda')
print(bycycles) # ['bmw', 'cannondale', 'honda', 'redline', 'specialized', 'ducati']
last_owned = bycycles.pop()
print(f"The last bycycle I owned was a {last_owned.title()}.") # The last bycycle I owned was a Ducati.
