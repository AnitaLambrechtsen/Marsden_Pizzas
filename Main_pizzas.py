# getting an integer from the user
def get_integer(m):
    user_input = int(input(m))
    return user_input


# getting a string from the user
def get_string(m):
    user_input = input(m)
    return user_input


# print big header line
def big_header():
    print("=~" * 60)


# print big header line
def line_header():
    print("-" * 60 * 2)


# printing the format for the pizza menu with index number
def pizza_menu(i):
    c = 0
    for x in i:
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
    line_header()
    user_input = get_string("Would you like pick-up (p) or delivery (d)? ")
    line_header()
    d['Type'] = user_input
    if user_input == "p":
        d['Name'] = get_string("What is your name for pick-up? ")
    if user_input == "d":
        d['Extras'] += 3
        d['Name'] = get_string("What is you name for delivery? ")
        d['Address'] = get_string("What is your address? ")
        d['Phone'] = get_integer("What is you phone number? ")
        line_header()
        print("${} has been added to your total for delivery".format(d['Extras']))
        line_header()
    print(d)
    return d


# adding pizzas to users order, passing through pizza_types, order and customer info
def add_to_order(p, o, d):
    line_header()
    pizza_menu(p)
    run = True
    while run is True:
        line_header()
        # asking user what pizza they want
        pizza = get_integer("Please enter the index number of the pizza you would like to order: ")
        quantity = get_integer("Please enter the number of {} pizzas that you would like: ".format(p[pizza][0]))
        line_header()
        # adding to order
        addition = [p[pizza][0], p[pizza][1], quantity]
        o.append(addition)
        # asking if they another kind of pizza
        add = get_string("Please enter 'y' if you would like to order something else, or 'n' to quit the function: ")
        line_header()
        # if they do:
        if add == "y":
            continue
        # if they don't:
        else:
            print("Your order is now:")
            big_header()
            print_customer_order(o)
            big_header()
            update_cost(d, o)
            print("Your cost for pizzas is now ${}".format(d['Cost']))
        # sending back to main function
        return p, o, d


def edit_order(o, d):
    big_header()
    print_customer_order(o)
    big_header()
    run = True
    while run is True:
        line_header()
        pizza = get_integer("Please enter the index number of the pizza that you would like to change the amount of: ")
        quantity = get_integer("Please enter the amount of {} pizzas that you would like: " 
                               "(or enter 0 to delete it from your order) ".format(o[pizza][0]))
        line_header()

        if quantity == 0:
            o.pop(pizza)
        if quantity > 0:
            o[pizza][2] = quantity

        update_cost(d, o)

        big_header()
        print_customer_order(o)
        big_header()
        print("Your cost for pizzas is now ${}".format(d['Cost']))
        big_header()

        add = get_string("Would you like to change anything else? Enter 'y' to continue, or 'n' to quit the function: ")
        if add == "y":
            continue
        if add == "n":
            return o, d


def main():
    # dictionary for users info
    customer_info = dict()
    # adding cost to dictionary
    customer_info['Cost'] = 0
    # adding extra costs to dictionary
    customer_info['Extras'] = 0

    # list of pizzas available to order with their cost
    pizza_types = [
        ["Easy Cheesy", 18.50],
        ["Pretty Plain Pepperoni", 18.50],
        ["Butchers", 18.50],
        ["The Better Person", 18.50]
    ]
    # main menu to run functions
    menu_list = [
        ["P", "Pizza types"],
        ["A", "Add pizza to order"],
        ["E", "Edit order"],
        ["I", "Customer order information (Pick-up/delivery)"],
        ["Q", "Quit"]
    ]
    # user order list
    order = [['Butchers', 18.5, 4], ["The Better Person", 18.5, 2]]

    # to run main menu
    run_program = True
    while run_program:
        big_header()
        # printing main menu in a presentable way
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        big_header()
        # asking user for their option and running what they choose
        user_choice = get_string("Please select an option: ")
        if user_choice == "P":
            big_header()
            pizza_menu(pizza_types)
            big_header()
        if user_choice == "A":
            add_to_order(pizza_types, order, customer_info)
        if user_choice == "E":
            edit_order(order, customer_info)
        if user_choice == "I":
            delivery_pickup(customer_info)
        if user_choice == "Q":
            big_header()
            print("Thank you, the program has ended")
            big_header()
            run_program = False


if __name__ == "__main__":
    big_header()
    print("Welcome to Marsden Pizzas!")
    big_header()
    main()
