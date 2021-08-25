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


def print_customer_details(d):
    c = 0
    for x, y in d.items():
        if x in ['Type', 'Name', 'Address', 'Phone']:
            output = "{}: {:<10}".format(x, y)
            print(output)
            c += 1
    return None


def update_cost(d, o):
    c = 0
    for x in o:
        c += x[1]*x[2]
    d["Cost"] = c
    return d, o


def init():
    d = {}
    d['Cost'] = 0
    d['Extras'] = 0
    return d


# asking user if they want delivery or pickup
def delivery_pickup(d):
    run = True
    if 'Type' in d:
        user_input = get_string('You already have set pickup or delivery, do you wish to set it again?')
        if user_input == "N":
            run = False
        else:
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
    while run is True:
        user_input = get_string("Would you like pick-up (p) or delivery (d)? ")
        d['Type'] = user_input
        if user_input == "p":
            d['Name'] = get_string("What is your name for pick-up? ")
            d['Type'] = "Pick-up"
        elif user_input == "d":
            d['Extras'] += 3
            d['Name'] = get_string("What is you name for delivery? ")
            d['Address'] = get_string("What is your address? ")
            d['Phone'] = get_integer("What is you phone number? ")
            print("${} has been added to your total for delivery".format(d['Extras']))
            d['Type'] = "Delivery"
        else:
            print("Please only enter 'p' or 'd'")
            continue
        print("Here are the customer details you have entered:")
        print_customer_details(d)
        change = get_string("Would you like to re-enter your customer information? Y/N ")
        if change == "Y":
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
            continue
        elif change == "N":
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
        add = get_string("Would you like to change anything else? Enter 'Y' to continue, or 'N' to quit the function: ")
        if add == "Y":
            continue
        elif add == "N":
            update_cost(d, o)
            print("Your cost is now ${}".format(d['Cost']))
            return p, o, d
        else:
            print("Please only enter 'Y' or 'N'")


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
        elif quantity > 0:
            o[pizza][2] = quantity

        update_cost(d, o)

        print_customer_order(o)
        print("Your cost is now ${}".format(d['Cost']))

        add = get_string("Would you like to change anything else? Enter 'Y' to continue, or 'N' to quit the function: ")
        if add == "Y":
            continue
        elif add == "N":
            return o, d


def review_order(o, d):
    c = 0
    update_cost(d, o)
    print("{:<20} {:<12} {:<8} {}".format("Type", "Amount", "Cost", "Sub-total"))
    print("-" * 54)
    for x in o:
        sub_amount = x[1]*x[2]
        output = "{:<20} x {:<10} @{:<7.2f} ${:.2f}".format(x[0], x[2], x[1], sub_amount)
        print(output)
        c += 1
    total_cost = d['Cost'] + d['Extras']
    print("{:<42} ${:.2f}".format("Extras", d["Extras"]))
    print("{:<42} ${:.2f}".format("Total cost", total_cost))


def confirm_order(o, d):
    print("Here is your order with your customer details:")
    review_order(o, d)
    print_customer_details(d)
    run = True
    while run is True:
        user_input = get_string("Would you like to confirm your order? Y/N or 'E' to return to the main menu: ")
        if user_input == "Y":
            print("Your order has been confirmed")
            print("You will be taken back to the main menu where you can make another one")
            d.clear()
            o.clear()
            return o, d
        elif user_input == "N":
            u_input = get_string("Would you like to cancel your order? (Y)es or 'E' to return to the main menu: ")
            if u_input == "Y":
                print("Your order has been cancelled")
                print("You will be taken back to the main menu where you can make another one")
                return [], init()
            elif u_input == "E":
                return o, d
        elif user_input == "E":
            return o, d


# main function
def main():
    customer_info = init()

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
        ["R", "Review pizzas ordered"],
        ["I", "Customer order information (Pick-up/delivery)"],
        ["C", "Confirm order"],
        ["Q", "Quit"]
    ]

    order = []
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
            if len(order) > 0:
                edit_order(order, customer_info)
            else:
                print("You haven't added anything to your order, please do that first")
        if user_choice == "I":
            delivery_pickup(customer_info)
        if user_choice == "R":
            if len(order) > 0:
                review_order(order, customer_info)
            else:
                print("You haven't added anything to your order, please do that first")
        if user_choice == "C":
            if len(order) > 0 and 'Type' in customer_info:
                confirm_order(order, customer_info)
            else:
                print("You haven't added anything to your order or you haven't set the delivery type")
            print(order, customer_info)
        if user_choice == "Q":
            run_program = False
        print(order, customer_info)


if __name__ == "__main__":
    main()
