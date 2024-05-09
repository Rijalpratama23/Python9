# input =  ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# output = ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

fruit = ["apel", "jeruk", "mangga"]
fruit2 = ["apel", "anggur", "nanas"]

fruit.extend(fruit2)
fruit.sort()
fruit.pop(1)


print(fruit)