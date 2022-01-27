# check the length of String
x = "Hello this is String example"
print(len(x))

# Multiple String
x = """ Hello this is a big paragraph
you need to take care of your self """
a = 'take' in x
print(a)


# check the if any String exists
x = "Hello this is String example."
a = 'Hello' in x
print(a)

# condition if String exist then only print
x = "Hello, India is a great country."
if 'UN' in x:
    print('India Found.')
else:
    print('opps!!')

# Convert in upper and lower case
countries = ["america","china","india"]
def checkFunction():
    x = "My country is - india"
    upperCaseCountry = []
    for country in countries:
        if (country == 'india'):
            print('India name is now in Upper case ',country.upper())
            upperCase = country.replace(country, country.upper())
            upperCaseCountry.append(upperCase)
            print(upperCaseCountry)

checkFunction()