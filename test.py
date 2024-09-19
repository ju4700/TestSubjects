bycycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycycles) # ['trek', 'cannondale', 'redline', 'specialized']
print(bycycles[0]) # trek

massage = f"My first Cycle was {bycycles[0].title()}."
print(massage) # My first Cycle was Trek.

bycycles[0] = 'honda'
print(bycycles) # ['honda', 'cannondale', 'redline', 'specialized']

bycycles.append('ducati')