from utility_functions import input_as_integer

# Next Class: Treasure hunt game using 2D array.

tickets = [
    ["Dhaka to Khulna", 200],
    ["Khulna to Dhaka", 200],
    ["Dhaka to Barishal", 400],
    ["Barishal to Dhaka", 400],
    ["Dhaka to Chittagong", 500],
    ["Chittagong to Dhaka", 500]
]

i = 0

while i < len(tickets):
    print(f"{i + 1}. {tickets[i][0]} - {tickets[i][1]}")
    i = i + 1

ticket_choice = input_as_integer("Choose train ticket: ")

if (ticket_choice > len(tickets)) or (ticket_choice < 1):  # if the user gives wrong input
    print(f"Please choose between 1 and {len(tickets)}")
else:  # If the user does NOT give wrong input
    print("You have chosen", tickets[ticket_choice - 1][0])
    number_of_tickets = input_as_integer("How many tickets do you want?: ")

    ticket_unit_price = tickets[ticket_choice - 1][1]

    total_ticket_price = number_of_tickets * ticket_unit_price
    
    # String formatting using f-string
    print(f"Your total ticket price is: {round(total_ticket_price, 2)} taka")
