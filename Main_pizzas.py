# getting an integer from the user
def get_integer(m):
    user_input = int(input(m))
    return user_input

# getting a string from the user
def get_string(m):
    user_input = input(m)
    return user_input

print("=~" * 50)
print("Welcome to Marsden Pizzas!")
print("=~" * 50)

# printing the format for the pizza menu
def pizza_menu(l):
    for x in l:
        output = "{:<25} -- ${}".format(x[0], x[1])
        print(output)
    return None

# asking user if they want delivery or pickup
def delivery_pickup(D):
    print("-" * 100)
    user_input = get_string("Would you like pick-up or delivery? ")
    print("-" * 100)
    D['Type'] = user_input
    # getting user information
    if user_input == "Pick-up":
        D['Name'] = get_string("What is your name for pick-up? ")
    if user_input == "Delivery":
        D['Cost'] += 3
        D['Name'] = get_string("What is you name for delivery? ")
        D['Address'] = get_string("What is your address? ")
        D['Phone'] = get_integer("What is you phone number? ")
        print("-" * 100)
        print("Your cost is now ${}".format(D['Cost']))
        print("-" * 100)
    return D

# adding pizzas to users order, passing through pizza_types, order and customer info
def add_to_order(L, O, D):
    run = True
    while run is True:
        print("-" * 100)
        # asking user what pizza they want
        pizza = get_integer("Please enter the index number of the pizza you would like to order: ")
        quantity = get_integer("Please enter the number of these pizzas that you would like: ")
        base = get_string("Would you like a plain or GF base for an additional $1? ")
        print("-" * 100)
        if base == "GF":
            D["Cost"] += 1
        # adding to order
        addition = [L[pizza][0], quantity, base]
        D["Cost"] += L[pizza][1]*quantity
        O.append(addition)
        add = get_string("Please enter 'y' if you would like to order something else, or anything to continue: ")
        print("-" * 100)
        if add == "y":
            continue
        else:
            print("Your cost is now ${}".format(D['Cost']))
            return L, O, D
            run = False

def main():
    customer_info = {}
    customer_info['Cost'] = 0

    pizza_types = [
        ["Easy Cheesy", 18.50],
        ["Pretty Plain Pepperoni", 18.50],
        ["Butchers", 18.50],
        ["The Better Person", 18.50]
    ]
    menu_list = [
        ["P", "Pizza types"],
        ["A", "Add to order"],
        ["Q", "Quit"]
    ]
    order = []

#    delivery_pickup(customer_info)
    run_program = True
    while run_program:
        print("=~" * 50)
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("=~" * 50)
        user_choice = get_string("Please select an option: ")
        if user_choice == "P":
            print("=~" * 50)
            pizza_menu(pizza_types)
            print("=~" * 50)
        if user_choice == "A":
            add_to_order(pizza_types, order, customer_info)
        if user_choice == "Q":
            print("=~" * 50)
            print("Thank you, the program has ended")
            print("=~" * 50)
            run_program = False

if __name__ == "__main__":
    main()