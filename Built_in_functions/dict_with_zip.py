keys = ["name", "age", "country"]
values = ["Jane", "30", "Canada"]

print(dict(zip(keys, values)))

bases = [8, 5, 2]
exponents = [2, 3, 4]

print(list(map(pow, bases, exponents)))