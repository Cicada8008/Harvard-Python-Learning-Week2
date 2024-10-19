#Math interpreter
# basic calculator that adds subtracts , mutiplies and divides 
#
expression = input("What is you math question ? e.g. '2 + 2' : ?")

x, y, z = expression.split(" ")

x = float(x)

z = float(z)

if y == ("+"):

    print(x + z)

elif y == ("-"):

    print(x - z)

elif y == ("*"):

    print(x * z)

else:

    print(x / z)
