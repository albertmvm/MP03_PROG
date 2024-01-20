#### Métode center(), ljust(), rjust().
##
string = "menú"
print("Métodes amb espais en blanc:")
print(string.center(10))
print(string.ljust(10))
print(string.rjust(10))

#### Metodes amb un caràcter.
##
print("\nMétodes amb caràcter:")
print(string.center(10, "="))
print(string.ljust(10, "="))
print(string.rjust(10, "="))

####Variable Modificada:
##
print("\nVariable modificada:")
string = string.center(6, "=")
print(string)

