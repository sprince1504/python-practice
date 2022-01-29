#hanlde the exception
#hanlde the exception
try:
    print(z)
except:
    print("variable not defined")
else:
    print("You got the error?")

# Exception
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")