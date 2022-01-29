# Print the touple
countries = ("India","Germany","France")
print(countries)

# Change the values in touple
countries = ("India","Germany","France")
new_countries = list(countries)
new_countries[1] = "France"
countries = tuple(new_countries)
print(countries)

# unpacking the tuples to variable  
countries = ("India","Germany","France")
(a,b,c) = countries
print(a)
print(b)
print(c)
