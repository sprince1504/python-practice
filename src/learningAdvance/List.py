# To print the value in list
myList = ["MH","MP","UP"]
print(myList)

# To print only specific values
myList = ["MH","1","MP","2","UP"]
print(myList[2:5])

# To interate the value
myList = ["MH","1","MP","2","UP"]
for x in myList:
    print(x)

# insert an element into list
myList = ["MH","1","MP","2","UP"]
myList.insert(1,"UK")
    print(x)

# mering two list
countries = ["India","USA","China"]
language = ["hi","en","hk"]
countries.extend(language)
print(countries)

# delete from list
countries = ["India","USA","China"]
del countries[2]
print(countries)

#while Loop
countries = ["MH","MP","UP","UK"]
i =0
while i<len(countries):
    print(countries[i])
    i = i+1

#find the String
countries = ["MH","MP","UP","UK"]
update = []
for x in countries:
    if "M" in x:
        update.append(x)
print(update)

#replace the element in String
fruits = ["apple","banana","grapes"]
fruits[1] = "ginger"
print(fruits)

# To add a list
append()

#To Merge the myList
extend()

# To insert
insert()

#Short syntaxing
countries = ["india","china","america","ok"]
newList = []
for x in countries:
    if "i" in x:
        newList.append(x.upper())
print(newList))

# matches list into another list
def countryFlag():
    regions = ["India","China","United States","Russia"]
    asia = ["India","China"]
    i = 0
    for x in asia:
        for y in regions:
            if x==y:
                print("Found")
countryFlag()

# Sort the lower String first
thislist = ["india", "China", "russia", "Germany"]
thislist.sort(key = str.lower)
print(thislist)
