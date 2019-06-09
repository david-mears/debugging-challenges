from pprint import pprint

stuff = {"name": "Charles",
         "age": 16,
         "in_school": True,
         "has_humor": False,
         "can_vote": False,
         "pet_name": "Boris",
         "best_friend": "Anna",
         "number_of_pets": 3}

result = []

# import pdb
# pdb.set_trace()

for key, value in stuff.items():
    if isinstance(value, bool):
        result.append(dict(name=key, type='bool',
                           value=value and 'true' or 'false'))
    elif isinstance(value, float):
        result.append(dict(name=key, value=value, type='float'))
    elif isinstance(value, int):
        result.append(dict(name=key, value=value, type='int'))
pprint(result)
