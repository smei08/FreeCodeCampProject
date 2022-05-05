#Madlibs, string concatenation with f strings
name = input("name: ")
noun = input("noun: ")
noun2 = input("noun2: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")

madlib = f"Hello, My name is {name}! I like to eat {noun} and drink {noun2}. \
    I also like to do {verb1}, it makes me so excited all the time. \
    Stay hydrated and {verb2}."

print(madlib)