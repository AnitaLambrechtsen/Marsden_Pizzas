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


# initial set up of main dictionary
def init():
    d = {}
    d['Cost'] = 0
    d['Extras'] = 0
    return d


# printing the format for the pizza menu with index number
def pizza_menu(i):
    c = 0
    for x in i:
        output = "{}: {:<25} -- ${}".format(c, x[0], x[1])
        print(output)
        c += 1
    return None


# printing out the pizzas ordered
def print_customer_order(o):
    c = 0
    for x in o:
        output = "{}: #{} {} pizzas".format(c, x[2], x[0])
        print(output)
        c += 1
    return None


# printing out the customer's details
def print_customer_details(d):
    c = 0
    for x, y in d.items():
        if x in ['Type', 'Name', 'Address', 'Phone']:
            output = "{}: {:<10}".format(x, y)
            print(output)
            c += 1
    return None


# calculating cost of the pizzas ordered
def update_cost(d, o):
    c = 0
    for x in o:
        c += x[1]*x[2]
    d["Cost"] = c
    return d, o


# asking user if they want delivery or pickup
def delivery_pickup(d):
    run = True
    # if the user has already entered the information:
    if 'Type' in d:
        user_input = get_string('You already have set pickup or delivery, do you wish to set it again? Y/N ')
        # sending back to main function
        if user_input == "N":
            run = False
        # if the user wishes to change what they previously entered
        elif user_input == "Y":
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
    # running the function
    while run is True:
        line_header()
        user_input = get_string("Would you like pick-up (p) or delivery (d)? ")
        line_header()
        d['Type'] = user_input
        if user_input == "p":
            d['Name'] = get_string("What is your name for pick-up? ")
            d['Type'] = "Pick-up"
        elif user_input == "d":
            d['Extras'] += 3
            d['Name'] = get_string("What is you name for delivery? ")
            d['Address'] = get_string("What is your address? ")
            d['Phone'] = get_integer("What is you phone number? ")
            d['Type'] = "Delivery"
            line_header()
            print("${} has been added to your total for delivery".format(d['Extras']))
            line_header()
        else:
            print("-")
            print("Please only enter 'p' or 'd'")
            print("-")
            continue
        line_header()
        print("Here are the customer details you have entered:")
        print_customer_details(d)
        line_header()
        change = get_string("Would you like to re-enter your customer information? Y/N ")
        line_header()
        # if they want to change what they have just entered
        if change == "Y":
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
            continue
        # sending back to main menu
        elif change == "N":
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
        elif add == "n":
            print("Your order is now:")
            big_header()
            print_customer_order(o)
            update_cost(d, o)
            print("The cost for your pizza(s) is now ${}".format(d['Cost']))
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
        # if the user wishes to remove a type of pizza
        if quantity == 0:
            o.pop(pizza)
        # if the user wants to change the amount of pizzas they have ordered
        elif quantity > 0:
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
        elif add == "n":
            return o, d


def review_order(o, d):
    c = 0
    update_cost(d, o)
    big_header()
    # printing headings of order review
    print("=~"*27)
    print("{:<20} {:<12} {:<8} {}".format("Type", "Amount", "Cost", "Sub-total"))
    print("-" * 54)
    # printing sub section with pizzas ordered and costs
    for x in o:
        sub_amount = x[1]*x[2]
        output = "{:<20} x {:<10} @{:<7.2f} ${:.2f}".format(x[0], x[2], x[1], sub_amount)
        print(output)
        c += 1
    # printing extras and total cost of order
    total_cost = d['Cost'] + d['Extras']
    print("=~"*27)
    print("{:<42} ${:.2f}".format("Extras", d["Extras"]))
    print("{:<42} ${:.2f}".format("Total cost", total_cost))
    print("=~"*27)


def confirm_order(o, d):
    print("Here is your order with your customer details:")
    review_order(o, d)
    print_customer_details(d)
    print("=~" * 27)
    big_header()
    run = True
    while run is True:
        # asking user if they wish to confirm
        line_header()
        user_input = get_string("Would you like to confirm your order? Y/N or 'E' to return to the main menu: ")
        line_header()
        # if yes:
        if user_input == "Y":
            line_header()
            print("Your order has been confirmed")
            print("You will be taken back to the main menu where you can make another one")
            line_header()
            # clearing order and sending to main function
            d.clear()
            o.clear()
            return o, d
        # if no:
        elif user_input == "N":
            # asking if they wish to cancel their order
            u_input = get_string("Would you like to cancel your order? (Y)es or 'E' to return to the main menu: ")
            # if yes:
            if u_input == "Y":
                line_header()
                print("Your order has been cancelled")
                print("You will be taken back to the main menu where you can make another one")
                line_header()
                # clearing order and sending to main function
                d.clear()
                o.clear()
                return o, d
            # sending to main function
            elif u_input == "E":
                return o, d
        elif user_input == "E":
            return o, d


def main():
    # creating main dictionary
    customer_info = init()

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
        ["R", "Review order"],
        ["C", "Confirm order"],
        ["Q", "Quit"]
    ]
    # user order list
    order = []

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
            # checking if they have entered their order
            if len(order) > 0:
                edit_order(order, customer_info)
            else:
                print("-")
                print("You haven't added anything to your order, please do that first")
                print("-")
        if user_choice == "I":
            delivery_pickup(customer_info)
        if user_choice == "R":
            # checking if they have entered their order
            if len(order) > 0:
                review_order(order, customer_info)
            else:
                print("-")
                print("You haven't added anything to your order, please do that first")
                print("-")
        if user_choice == "C":
            # checking if they have entered their order and customer order
            if len(order) > 0 and 'Type' in customer_info:
                confirm_order(order, customer_info)
            else:
                print("-")
                print("You haven't added anything to your order or customer details, please do that first")
                print("-")
        if user_choice == "Q":
            big_header()
            print("Thank you, the program has ended")
            big_header()
            run_program = False


# running main function and opening message
if __name__ == "__main__":
    big_header()
    print("Welcome to Marsden Pizzas!")
    big_header()
    main()
