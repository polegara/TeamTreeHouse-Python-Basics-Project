TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100  

# Create the calculate_price function. It takes the number of tickets and returns
# TICKET_PRICE * amount_of_tickets
def calculate_price(amount_of_tickets):
    # Create a new constant for $2 service charge
    # Add service charge to our result
    return (TICKET_PRICE * amount_of_tickets) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets reamining.".format(tickets_remaining))
    name = input("What is your name? ")
    amount_of_tickets = int(input("How many tickets would you like to buy, {}? ".format(name)))
    try:
        amount_of_tickets = int(amount_of_tickets)
        if amount_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh now, we ran into an issue! {} Please try again! ".format(err))
    else:
        price = calculate_price(amount_of_tickets)
        print("{}, you owe ${} for {} tickets.\nPlease note that there is a service charge with this transaction of ${}. ".format(name, price, amount_of_tickets, SERVICE_CHARGE))
        buy_tickets = input("Would you like to proceed? (Y or N) ")
        if buy_tickets.lower() == "y":
            #TODO: Gather Credit Card information and process it.
            print("SOLD!")
            tickets_remaining -= amount_of_tickets
            print("There are {} tickets remaining for the show! ".format(tickets_remaining))
        else:
            print("Thanks for looking, {}! ".format(name))
print("Sorry the tickets are sold out!!! :(")