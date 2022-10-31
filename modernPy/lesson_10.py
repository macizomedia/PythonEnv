from collections import defaultdict
# Defaultdict is a dictionary that has a default value for keys that don't exist
b = {'a': 1, 'b': 2, 'c': 3}

x = defaultdict(lambda: -1)

x['a'] = 1
# if the value is not in the dictionary, it will return the default value
print(x['b'])