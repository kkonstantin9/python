def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key].append(value)
    else:
        new_key = key * 2
        if new_key not in d:
            d[new_key] = []
        d[new_key].append(value)

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
