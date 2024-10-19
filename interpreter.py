#Math interpreter
expression = input("what is you math question ?")

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
