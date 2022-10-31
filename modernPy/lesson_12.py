from collections import defaultdict
from pprint import pprint

example = defaultdict(list)

# Defaultdict for gruping and accumulating values

# Example 1 one to many list

eng2Spanish = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis'],
}

# Reverse the dictionary

for eng, spanish in eng2Spanish.items():
    for s in spanish:
        example[s].append(eng)

pprint(example)

# Example 2 one to one dict bijective mapping

e2s = {
    'hola': 'hello',
    'chao': 'bye',
    'hasta luego': 'see you later',
    'placer conocerte': 'nice to meet you',
}

#  Reverse the dictionary

pprint({spanish: eng for eng, spanish in e2s.items()})