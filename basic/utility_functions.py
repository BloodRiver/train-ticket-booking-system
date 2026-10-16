def input_as_integer(message):
    while True:
        try:
            value = int(input(message))
        except ValueError:  # If a ValueError occurs, do this:
            print("Invalid input. Please enter a whole number.")
        else:  # If no error occurs
            return value


# number_of_tickets = input_as_integer("How many tickets do you want?: ")
