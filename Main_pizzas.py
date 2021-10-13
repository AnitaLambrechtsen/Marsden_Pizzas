import re
"""
 Main pizza program for ordering pizzas, with functions that allow a user to:
 add a pizza to their order, 
 edit their order, 
 enter personal information for pick-up or delivery, 
 review and 
 confirm their order.
 Main program is ran in the main function.
"""


def get_integer(m, minimum, *maximum):
    """
        Transferable function for an integer input with a message, minimum value and optional list for maximum value.
        Checks that the user's input is greater than the minimum and smaller than the optional maximum.

        :param m: string message
        :param minimum: integer
        :optional param maximum: integer list
        :return: integer input
    """
    # setting the validation loop
    incorrect_input = True
    # creating empty user_input
    user_input = ""
    while incorrect_input:
        # if the user has entered an integer:
        try:
            user_input = int(input(m))
            if len(maximum) > 0 and maximum[0] == minimum and user_input != minimum:
                print("-")
                print("Please enter an input of {}".format(minimum))
                print("-")
            # if the user has entered an integer less than the minimum or an integer greater than the maximum
            elif len(maximum) > 0 and (minimum > user_input or user_input > maximum[0]):
                print("-")
                print("Please enter an input greater than or equal to {} and less than or equal to {}".format
                      (minimum, maximum[0]))
                print("-")
            # if the user has entered an integer less than the minimum
            elif minimum > user_input:
                print("-")
                print("Please enter an input greater than or equal to {}".format(minimum))
                print("-")
            # if all good, ends the loop
            else:
                incorrect_input = False
        # if the user has not entered an integer:
        except ValueError:
            print("-")
            print("Please enter an integer")
            print("-")
    # returns input once correct input given
    return user_input


def get_string(m, minimum, *maximum):
    """
        Transferable function for a string input with a message, minimum value and optional list for maximum value.
        Checks that the user's input is greater than the min, smaller than the optional max and makes input titled.

        :param m: string message
        :param minimum: integer
        :param maximum: integer list
        :return: string input
    """
    # setting the validation loop
    incorrect_input = True
    # creating empty user_input
    user_input = ""
    while incorrect_input:
        # making user_input a string
        user_input = input(m)
        # if the user has entered an input:
        if user_input:
            user_input = user_input.title()
            # if the user has entered a string less than the minimum or greater than the maximum
            if len(maximum) > 0 and (minimum > len(user_input) or len(user_input) > maximum[0]):
                print("-")
                print("Please enter an input greater than or equal to {} and less than or equal to {}".format
                      (minimum, maximum[0]))
                print("-")
            # if the users input is less than the minimum
            elif len(user_input) < minimum:
                print("-")
                print("Please enter an input greater than {}".format(minimum))
                print("-")
            else:
                # if all good, end the loop
                incorrect_input = False
        # if the user has not entered anything
        else:
            print("-")
            print("You have not entered anything, please do")
            print("-")
    return user_input


def single_string(m, answers, *error_message):
    """
        Transferable function for a string input that is one character long, with a correct input and optional list for
        a particular error message.
        Checks if the user's input is one character and the correct input, prints out error message if found

        :param m: string message
        :param answers: string
        :param error_message: string list
        :return: string input
    """
    # setting validation loop
    incorrect_input = True
    # creating empty user_input
    user_input = ""
    while incorrect_input:
        # making user_input a string
        user_input = input(m)
        # if user has entered an answer larger than one character
        if len(user_input) > 1 or len(user_input) < 1:
            print("-")
            print("You have entered an incorrect input, please enter a singular letter")
            print("-")
        # if user has entered an input and is a correct input
        elif user_input and user_input.upper() in answers:
            # if all good exit loop
            incorrect_input = False
        # if input is still incorrect
        else:
            # if there is a unique error message
            if error_message:
                print("-")
                print(error_message[0])
                print("-")
            else:
                # if there is more than two possible correct inputs, to give a clear error message to the user
                if len(answers) > 2:
                    answer = ', '.join(answers[:-1]) + ' or ' + answers[-1]
                # if there is only two correct inputs
                else:
                    answer = ' or '.join(answers)
                print("-")
                print("Sorry, your input is incorrect, please enter " + answer)
                print("-")
    return user_input.upper()


def phone_number(m):
    """
        Function to get the user's telephone number with validation for the input of a New Zealand number
        Using https://en.wikipedia.org/wiki/Telephone_numbers_in_New_Zealand as a reference

        :param m: string message
        :return: string input
    """
    # setting validation loop
    incorrect_input = True
    return_value = ""
    while incorrect_input:
        user_input = input(m)
        result = re.sub("[^\d+]", '', user_input)
        if result.startswith('0'):
            # Starts with 03/04/06/07/09 for National Numbers
            if re.match('0[34679]', result) and len(result) == 9:
                return_value = "{}-{}-{}".format(result[0:2], result[2:5], result[5:])
                incorrect_input = False
            # Starts with 021/022/027/028 for Mobile Numbers
            if re.match('02[1279]', result) and len(result) in range(9, 13):
                return_value = "{}-{}-{}".format(result[0:3], result[3:6], result[6:])
                incorrect_input = False
        # Starts with 3 to 9 and 7 digits for Local Numbers
        if re.match('[2-9]', result) and len(result) == 7:
            return_value = "{}-{}".format(result[0:3], result[3:])
            incorrect_input = False
        if incorrect_input:
            print("-")
            print("Please enter a valid New Zealand phone number as '{}' is not valid".format(result))
            print("-")
    return return_value


def big_header():
    """
        Function for styling the divide of a main header

        :return: none
    """
    print("=~" * 60)


def line_header():
    """
        Function for styling the divide of a sub-header

        :return: none
    """
    print("-" * 60 * 2)


def init():
    """
        Function to initially set up the main dictionary containing customer information

        :return: dictionary
    """
    d = dict()
    d['Cost'] = 0
    d['Extras'] = 0
    return d


def pizza_menu(i):
    """
        Function to print the pizza menu with indexes

        :param i: list
        :return: list
    """
    c = 0
    for x in i:
        output = "{}: {:<25} -- ${}".format(c, x[0], x[1])
        print(output)
        c += 1
    return None


def print_customer_order(o):
    """
        Function to print the customer's ordered pizzas with indexes from a list

        :param o: list
        :return: none
    """
    c = 0
    for x in o:
        output = "{}: #{} {} pizzas".format(c, x[2], x[0])
        print(output)
        c += 1
    return None


def print_customer_details(d):
    """
        Function to print out the customer's details from a dictionary

        :param d: dictionary
        :return: none
    """
    for x, y in d.items():
        if x in ['Type', 'Name', 'Address', 'Phone']:
            output = "{}: {:<10}".format(x, y)
            print(output)
    return None


def update_cost(d, o):
    """
        Function to calculate the cost of the pizzas that the user ordered

        :param d: dictionary
        :param o: list
        :return: both
    """
    c = 0
    for x in o:
        c += x[1]*x[2]
    d["Cost"] = c
    return d, o


def delivery_pickup(d):
    """
        Function that allows the user to select their method of collection and requires information accordingly that is
        stored in a dictionary

        :param d: dictionary
        :return: dictionary
    """
    # if the user has already entered the information:
    if 'Type' in d:
        user_input = single_string("You already have set your information, do you wish to set it again? Y/N ",
                                   ['Y', 'N'])
        # sending back to main function
        if user_input == "N":
            return d
        # if the user wishes to change what they previously entered
        else:
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
    # running the function
    while True:
        line_header()
        # asking for user input
        user_input = single_string("Would you like pick-up 'P' or delivery 'D' (for additional $3 charge)? ",
                                   ['P', 'D'])
        line_header()
        d['Type'] = user_input

        # validating the user's entry for their name
        get_name = True
        while get_name:
            d['Name'] = get_string("What is your name for this order? ", 2, 30)
            # prints out a question if it is not what the regex searched for
            # regex searches for capital and lower-case letters, hyphens and spaces
            if re.search('^[A-Za-z- ]+$', d['Name']):
                get_name = False
            else:
                print("-")
                print("Please only enter letters of the alphabet (hyphen included) for your name")
                print("-")

        # following information for dictionary required based on their input
        if user_input == "P":
            d['Type'] = "Pick-up"
        else:
            d['Extras'] += 3
            d['Address'] = get_string("What is your address? ", 5, 50)
            d['Phone'] = phone_number("What is you phone number? ")
            d['Type'] = "Delivery"
            line_header()
            print("${} has been added to your total for delivery".format(d['Extras']))

        # printing what the user has given
        line_header()
        print("Here are the customer details you have entered:")
        print_customer_details(d)
        line_header()

        # if they want to change what they have just entered
        change = single_string("Would you like to re-enter your customer information? Y/N ", ['Y', 'N'])
        if change == "Y":
            # deleting what they have just entered to re-enter
            keys_to_remove = ['Name', 'Type', 'Address', 'Phone']
            for key in keys_to_remove:
                if key in d:
                    del d[key]
            d['Extras'] = 0
        else:
            # sending back to main menu if all good
            return d


def add_to_order(p, o, d):
    """
        Function that allows a user to add to their order, duplicating values from the pizza list, adding to their
        order list with the quantity

        :param p: list
        :param o: list
        :param d: dictionary
        :return: all
    """
    line_header()
    # printing the pizza menu again to remind the user
    pizza_menu(p)
    while True:
        line_header()
        # asking user what pizza they want and how much
        pizza = get_integer("Please enter the index number of the pizza you would like to order: ", 0, 9)
        quantity = get_integer("Please enter the number of {} pizzas that you would like: ".format(p[pizza][0]), 1, 10)
        line_header()

        # ensuring that if the user wants more of a certain pizza type, it will not appear twice in the menu
        order_updated = False
        c = 0
        # if the pizza type is already in their order
        for current_o in o:
            if current_o[0] == p[pizza][0]:
                o[c][2] = current_o[2] + quantity
                order_updated = True
            c += 1
        # if the pizza is not present in their order, then adds new type and amount
        if not order_updated:
            addition = [p[pizza][0], p[pizza][1], quantity]
            o.append(addition)

        # asking if they want to add another pizza to their order
        add = single_string("Please enter 'Y' if you would like to order something else, or 'N' to quit the function: ",
                            ['Y', 'N'])
        # if not, print what they have ordered with the cost and return values
        if add == "N":
            print("Your order is now:")
            big_header()
            print_customer_order(o)
            update_cost(d, o)
            print("The cost for your pizza(s) is now ${}".format(d['Cost']))
            return p, o, d


def edit_order(o, d):
    """
    Function that allows the user to edit their order, change the quantity what they have currently ordered and remove
    certain types, changes stored in list and dictionary

    :param o: list
    :param d: dictionary
    :return: both
    """
    big_header()
    # printing what they have ordered to remind the user
    print_customer_order(o)
    big_header()
    while True:
        line_header()
        # asking for users input
        pizza = get_integer("Please enter the index number of the pizza that you would like to change the amount of: ",
                            0, len(o)-1)
        quantity = get_integer("Please enter the amount of {} pizzas that you would now like: " 
                               "(or enter 0 to delete it from your order) ".format(o[pizza][0]), 0, 10)
        # if the user wishes to remove a type of pizza
        if quantity == 0:
            o.pop(pizza)
        # if the user wants to change the amount of pizzas they have ordered
        else:
            o[pizza][2] = quantity

        update_cost(d, o)
        # printing their updated order and cost
        big_header()
        print_customer_order(o)
        big_header()
        print("Your cost for pizzas is now ${}".format(d['Cost']))
        big_header()

        # asking user if they wish to edit anything else
        add = single_string("Would you like to change anything else? Enter 'Y' to continue, or 'N' to quit the "
                            "function: ", ['Y', 'N'])
        if add == "N":
            return o, d


def review_order(o, d):
    """
    Function that allows a user to view their current order

    :param o: list
    :param d: dictionary
    :return: both
    """
    c = 0
    update_cost(d, o)
    # printing headings of order review
    print("=~"*28)
    print("{:<24} {:<12} {:<8} {}".format("Type", "Amount", "Cost", "Sub-total"))
    print("-" * 56)
    # printing sub section with pizzas ordered and costs
    for x in o:
        sub_amount = x[1]*x[2]
        output = "{:<24} x {:<10} @{:<7.2f} ${:.2f}".format(x[0], x[2], x[1], sub_amount)
        print(output)
        c += 1
    # printing extras and total cost of order
    total_cost = d['Cost'] + d['Extras']
    print("=~"*28)
    print("{:<46} ${:.2f}".format("Extras", d["Extras"]))
    print("{:<46} ${:.2f}".format("Total cost", total_cost))
    print("=~"*28)


def confirm_order(o, d):
    """
        Function allowing the user to view and finalise their order, that will be stored and cleared

        :param o: list
        :param d: dictionary
        :return: both
    """
    line_header()
    # printing their order and details to remind the user before confirming
    print("Here is your order with your customer details:")
    review_order(o, d)
    print_customer_details(d)
    print("=~" * 28)
    while True:
        # asking user if they wish to confirm
        line_header()
        user_input = single_string("Would you like to confirm your order? Y/N or 'E' to return to the main menu: ",
                                   ['Y', 'N', 'E'])
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
            u_input = single_string("Would you like to cancel your order? (Y)es or 'E' to return to the main menu: ",
                                    ['Y', 'E'])
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
            else:
                return o, d
        # sending to main function
        else:
            return o, d


def main():
    """
        Main function to run the program and all of the functions within it

        :return: none
    """
    # creating main dictionary
    customer_info = init()

    # list of pizzas available to order with their cost
    pizza_types = [
        ["Easy Cheesy", 13],
        ["Majestic Margherita", 13],
        ["Pretty Plain Pepperoni", 13],
        ["Spicy Jalapeño", 15.50],
        ["The 5+ a Day", 15.50],
        ["Butchers", 15.50],
        ["The Better Person", 15.50],
        ["Sweet Tooth", 15.50],
        ["Chicago Styled", 18],
        ["The Works", 18]
    ]
    # main menu dictionary to run functions
    menu_dict = {
        "P": "Pizza types",
        "A": "Add pizza to order",
        "E": "Edit order",
        "R": "Review pizzas ordered",
        "I": "Customer order information (Pick-up/delivery)",
        "C": "Confirm order",
        "Q": "Quit"
    }

    # user's order list
    order = []

    # to run main menu
    run_program = True
    while run_program:
        big_header()
        # printing main menu in a presentable way
        for x, y in menu_dict.items():
            output = "{}: {}".format(x, y)
            print(output)
        big_header()
        # asking user for their option and running what they choose
        user_choice = single_string("Please select an option: ", list(menu_dict.keys()), "You have entered an incorrect"
                                    " input, please enter a letter present in the menu above")
        if user_choice == "P":
            line_header()
            pizza_menu(pizza_types)
            line_header()
        if user_choice == "A":
            add_to_order(pizza_types, order, customer_info)
        if user_choice in ["E", "R"]:
            # checking if they have entered their pizza order before running functions
            if len(order) > 0:
                if user_choice == "E":
                    edit_order(order, customer_info)
                else:
                    review_order(order, customer_info)
            else:
                print("-")
                print("You haven't added anything to your order yet! Please do that by selecting 'A'")
                print("-")
        if user_choice == "I":
            delivery_pickup(customer_info)
        if user_choice == "C":
            # checking if they have entered their pizza order and customer customer details before running function
            if len(order) > 0 and 'Type' in customer_info:
                confirm_order(order, customer_info)
            else:
                print("-")
                print("You haven't added anything to your order or customer details yet! Please do that by"
                      " selecting 'A' and/or 'I' in the main menu")
                print("-")
        if user_choice == "Q":
            # checking if they have already started entering information before quitting
            if len(order) > 0 or 'Type' in customer_info:
                run = True
                while run is True:
                    # asking if they would still wish to quit
                    print('-')
                    print("You have already started an order and not yet confirmed it")
                    user_input = single_string("Are you sure you wish to quit the program? Y/N: ", ['Y', 'N'])
                    print('-')
                    # if yes, ending loop to quit the program
                    if user_input == "Y":
                        run = False
                        run_program = False
                    # if no, returning to main menu
                    if user_input == "N":
                        print("You are returning to the main menu")

            else:
                # asking user if they still wish to quit, even without entering anything
                user_input = single_string("Are you sure you wish to quit the program? Y/N: ", ['Y', 'N'])
                print('-')
                # if yes, ending loop to quit the program
                if user_input == "Y":
                    run_program = False
                # if no, returning to main menu
                if user_input == "N":
                    print("You are returning to the main menu")
                # quitting program
            big_header()
            print("Thank you, the program has ended")
            big_header()
            run_program = False


# running main function and opening message
if __name__ == "__main__":
    print("Welcome to Marsden Pizzas!")
    main()
