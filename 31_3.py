# PLAN:
# create a list
#   (its gonna be humongous)
# put the first seed list in it ([200])
# for every list in the big list:
#   for every unique value in list,
#       split it, put it back into the list, and add the new list into the big list
# At the end, count em and weep cause it aint right

values = [ 1, 2, 5,
        10, 20, 50, 
        100, 200 ]


def split(value):
    if value in {10, 100, 2, 20, 200}:
        return [value/2, value/2]
    elif value in {5, 50}:
        return [value*2/5, value*2/5, value/5]


combos = [ [200] ]

for combo in combos:
    for value in set(combo):
        if value == 1:
            continue

        copy = combo.copy()

        copy.remove(value)
        copy.extend(split(value))
        copy.sort(reverse=True)

        if copy not in combos:
            combos.append(copy)

print(len(combos))

# for combo in combos:
#     print(combo)
