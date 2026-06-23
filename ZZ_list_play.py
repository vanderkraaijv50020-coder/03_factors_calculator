import random

all_numbers = []

for item in range(0, 6):

    # generate a random number
    mystery_num = random.randint(1, 10)

    if mystery_num not in all_numbers:
        all_numbers.append(mystery_num)

all_numbers.sort()
print(all_numbers)

print(len(all_numbers))

# check if it's odd
if len(all_numbers) %2 ==1:
    print("that's odd")
else:
    print("That's not odd at all.")