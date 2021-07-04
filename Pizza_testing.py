# getting an integer from the user
def get_integer(m):
    user_input = int(input(m))
    return user_input

# getting a string from the user
def get_string(m):
    user_input = input(m)
    return user_input

# printing the format for the pizza menu
def pizza_menu(L):
    for x in L:
        output = "{:<25} -- ${}".format(x[0], x[1])
        print(output)
    return None

# asking user if they want delivery or pickup
def delivery_pickup(D):
    user_input = get_string("Would you like pick-up or delivery? ")
    D['Type'] = user_input
    if user_input == "Pick-up":
        D['Name'] = get_string("What is your name for pick-up? ")
    if user_input == "Delivery":
        D['Cost'] += 3
        D['Name'] = get_string("What is you name for delivery? ")
        D['Address'] = get_string("What is your address? ")
        D['Phone'] = get_integer("What is you phone number? ")
        print("Your cost is now ${}".format(D['Cost']))
    return D

def add_to_order(L, O, D):
    run = True
    while run is True:
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ")
        quantity = get_integer("Please enter the number of these pizzas that you would like: ")
        base = get_string("Would you like a plain or GF base for an additional $1? ")
        if base == "GF":
            D["Cost"] += 1
        addition = [L[pizza][0], quantity, base]
        D["Cost"] += L[pizza][1]*quantity
        print("Your cost is now ${}".format(D['Cost']))
        O.append(addition)
        add = get_string("Would you like to order anything else? Enter 'y' to continue, or anything else to quit. ")
        if add == "y":
            continue
        else:
            return L, O, D
            run = False

def main():
    customer_info = {}
    customer_info['Cost'] = 0

    pizza_types = [
        ["Easy Cheesy", 13],
        ["Pretty Plain Pepperoni", 15],
        ["Butchers", 18],
        ["The Better Person", 18]
    ]
    menu_list = [
        ["P", "Pizza types"],
        ["A", "Add to order"],
        ["Q", "Quit"]
    ]

    order = []

#    delivery_pickup(customer_info)
#    print(customer_info)
    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ")
        if user_choice == "P":
            pizza_menu(pizza_types)
        if user_choice == "A":
            add_to_order(pizza_types, order, customer_info)
            print(order)
        if user_choice == "Q":
            run_program = False

if __name__ == "__main__":
    main()