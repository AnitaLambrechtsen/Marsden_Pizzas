# getting an integer from the user
def get_integer(m):
    user_input = int(input(m))
    return user_input


# getting a string from the user
def get_string(m):
    user_input = input(m)
    return user_input


# printing the format for the pizza menu
def pizza_menu(r):
    c = 0
    for x in r:
        output = "{}: {:<25} -- ${}".format(c, x[0], x[1])
        print(output)
        c += 1
    return None


def print_customer_order(o):
    c = 0
    for x in o:
        output = "{}: #{} {} pizzas".format(c, x[2], x[0])
        print(output)
        c += 1
    return None


def update_cost(d, o):
    c = 0
    for x in o:
        c += x[1]*x[2]
    d["Cost"] = c
    return d, o


# asking user if they want delivery or pickup
def delivery_pickup(d):
    user_input = get_string("Would you like pick-up (p) or delivery (d)? ")
    d['Type'] = user_input
    if user_input == "p":
        d['Name'] = get_string("What is your name for pick-up? ")
    if user_input == "d":
        d['Extras'] += 3
        d['Name'] = get_string("What is you name for delivery? ")
        d['Address'] = get_string("What is your address? ")
        d['Phone'] = get_integer("What is you phone number? ")
        print("${} has been added to your total for delivery".format(d['Extras']))
    return d


# adding pizza to order
def add_to_order(p, o, d):
    pizza_menu(p)
    run = True
    while run is True:
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ")
        quantity = get_integer("Please enter the number of {} pizzas that you would like: ".format(p[pizza][0]))
        addition = [p[pizza][0], p[pizza][1], quantity]
        o.append(addition)
        add = get_string("Would you like to change anything else? Enter 'y' to continue, or 'n' to quit the function: ")
        if add == "y":
            continue
        else:
            update_cost(d, o)
            print("Your cost is now ${}".format(d['Cost']))
        return p, o, d


# editing or deleting pizza
def edit_order(o, d):
    print_customer_order(o)
    run = True
    while run is True:
        pizza = get_integer("Please enter the index number of the pizza that you would like to change the amount of: ")
        quantity = get_integer("Please enter the amount of {} pizzas that you would like to now have: (or enter 0 to"
                               " delete the type) ".format(o[pizza][0]))

        if quantity == 0:
            o.pop(pizza)
        if quantity > 0:
            o[pizza][2] = quantity

        update_cost(d, o)

        print_customer_order(o)
        print("Your cost is now ${}".format(d['Cost']))

        add = get_string("Would you like to change anything else? Enter 'y' to continue, or 'n' to quit the function: ")
        if add == "y":
            continue
        if add == "n":
            return o, d


# main function
def main():
    customer_info = {}
    customer_info['Cost'] = 0
    customer_info['Extras'] = 0

    pizza_types = [
        ["Easy Cheesy", 13],
        ["Pretty Plain Pepperoni", 15],
        ["Butchers", 18],
        ["The Better Person", 18]
    ]
    menu_list = [
        ["P", "Pizza types"],
        ["A", "Add pizza to order"],
        ["E", "Edit order"],
        ["I", "Customer order information (Pick-up/delivery)"],
        ["Q", "Quit"]
    ]

    order = []
    # ['Butchers', 18, 4], ["The Better Person", 18, 2]
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
        if user_choice == "E":
            edit_order(order, customer_info)
        if user_choice == "I":
            delivery_pickup(customer_info)
        if user_choice == "Q":
            run_program = False


if __name__ == "__main__":
    main()
