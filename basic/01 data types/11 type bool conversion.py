
print(bool()) # False

# falsy values
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False
print(bool("")) # False
print(bool(None)) # False

print(bool(True)) # True
print(bool(10)) # True
print(bool(-10)) # True
print(bool(-12.56)) # True
print(bool((1,2,3))) # True
print(bool([0])) # True
print(bool({0})) # True
print(bool("x")) # True