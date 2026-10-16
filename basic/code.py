from utility_functions import input_as_integer

ticket_unit_price = 200.5567

print("1. Dhaka to Khulna")
print("2. Khulna to Dhaka")
print("3. Dhaka to Barishal")
print("4. Barishal to Dhaka")

ticket_choice = input_as_integer("Choose train ticket: ")

if (ticket_choice > 4) or (ticket_choice < 1):  # if the user gives wrong input
    print("Please choose between 1 and 4")
else:  # If the user does NOT give wrong input
    number_of_tickets = input_as_integer("How many tickets do you want?: ")

    total_ticket_price = number_of_tickets * ticket_unit_price
    
    # String formatting using f-string
    print(f"Your total ticket price is: {round(total_ticket_price, 2)} taka")
