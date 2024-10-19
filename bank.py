#Home Federal Savings Bank
# If input is Hello user gets $0
# if user input begins with H user gets $20
# if nothing is entered user gets $100 dollars 
# sceane made famous by Seinfeld scene 7 ep 24

def main():

    greeting = input("Greeting: ").strip().lower()



    if is_hello(greeting):

        print("$0")

    elif is_h(greeting):

        print("$20")

    else:

        print("$100")





def is_hello(greeting):

    return greeting.startswith("hello")  # Check if greeting starts with "hello"



def is_h(greeting):

    return greeting.startswith("h") and not greeting.startswith("hello")  # Check if greeting starts with "h" but is not "hello"





if __name__ == "__main__":

    main()
