##New Project##

guests = ["Fatima", "Mariam", "Safa"]


print(f"You're invited to dinner, {guests[0]}")
print(f"You're invited to dinner, {guests[1]}")
print(f"You're invited to dinner, {guests[2]}")

# Mariam can't make it
print(f"\nSorry, {guests[1]} can't make it to dinner.")

# Replace Mariam with a new guest
guests[1] = "Aisha"

# Printing the invitations again
print("\nUpdated invitations:")
print(f"You're invited to dinner, {guests[0]}")
print(f"You're invited to dinner, {guests[1]}")
print(f"You're invited to dinner, {guests[2]}")
