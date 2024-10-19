#Famous sceane Hitchhikers guide to the galaxy !
#playing with match and case function . 

name = input("What is the Answer to the Great Question of Life,").strip().lower()



match name:

    case "42"|"forty-two"|"forty two":

        print("Yes")

    case _:

        print("No")

