## NEW PROJECT

guests = ('fatima', 'Mariam', 'Safa')

msg = f'Youre invited to dinner, {guests[0].title()}'
print(msg)

msg = f'Youre invited to dinner, {guests[1].title()}'
print(msg)

msg = f'Youre invited to dinner, {guests[2].title()}'
print(msg)

guests = ["Fatima", "Mariam", "Safa"]


print(f"You're invited to dinner, {guests[0]}")
print(f"You're invited to dinner, {guests[1]}")
print(f"You're invited to dinner, {guests[2]}")

# Mariam can't make it
print(f"Sorry, {guests[1]} can't make it to dinner.")

# Replace Mariam with a new guest
guests[1] = "Aisha"

# Printing the invitations again
print("\nUpdated invitations:")
print(f"You're invited to dinner, {guests[0]}")
print(f"You're invited to dinner, {guests[1]}")
print(f"You're invited to dinner, {guests[2]}")

# Not enough room in table
print("\nSorry, there is no enough room in table only 2 guests can be invited")

name = guests.pop()
print (f"Sorry, {name.title()} there is no enough room in table")

# those who got the invitations

name = guests[0].title()
print(f"{name}, youre still invited.")

name = guests[1].title()
print(f"{name}, youre still invited")

#Empty out the list
del(guests[0])
del(guests[0])

#Proving the list is empty
print(guests)


