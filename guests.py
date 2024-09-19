invitation = ['Alice', 'Bob', 'Charlie']
print(f"PLease come to the party, {invitation[0].title()}.")
print(f"PLease come to the party, {invitation[1].title()}.")
print(f"PLease come to the party, {invitation[2].title()}.")

print("Unfortunately, Bob can't make it to the party.")
invitation[1] = 'David'
print(f"PLease come to the party, {invitation[0].title()}.")
print(f"PLease come to the party, {invitation[1].title()}.")
print(f"PLease come to the party, {invitation[2].title()}.")
print("We found a bigger table!")

invitation.insert(0, 'Eve')
invitation.insert(1, 'Frank')
invitation.append('Grace')

for guest in invitation:
    print(f"PLease come to the party, {guest.title()}.")

print("Sorry, we can only invite two guests.")

while len(invitation) > 2:
    popped_guest = invitation.pop()
    print(f"Sorry, {popped_guest.title()}, we can't invite you to the party.")

for guest in invitation:
    print(f"PLease come to the party, {guest.title()}.")

del invitation[0]
del invitation[0]

print(invitation)

l = ['Canada', 'Germany', 'USA', 'Switzerland', 'Russia']

print(l)
print(sorted(l))
print(l)
print(sorted(l, reverse=True))
l.reverse()
print(l)
l.reverse()
print(l)
