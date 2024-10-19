def main():

    time = input("What time is it ")





    period = ""

    if "AM" in time.upper():

        period = "AM"

        time = time.upper().replace("AM", "").strip()  # Remove 'AM'

    elif "PM" in time.upper():

        period = "PM"

        time = time.upper().replace("PM", "").strip()  # Remove 'P

    time_in_hours = convert(time)



    if 7 <= time_in_hours <=8:

        print("breakfast time")

    elif 12<= time_in_hours <=13:

        print("lunch time")

    elif 18<= time_in_hours <=19:

        print("dinner time")

    else:

        print("Its not time to eat")



def convert(time):

    hours, minutes = time.split(":")



    hours = int(hours)

    minutes = int(minutes)



    return hours + minutes / 60





if __name__ == "__main__":

    main()

 