def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

print("=~" * 30)
print("Welcome to Marsden Pizzas!")
print("=~" * 30)

def pizza_menu(l):
    for x in l:
        output = "{:<25} -- ${}".format(x[0], x[1])
        print(output)
    return None

def delivery_pickup(D):
    print("-" * 60)
    user_input = get_string("Would you like pick-up or delivery? ")
    print("-" * 60)
    D['Type'] = user_input
    if user_input == "Pick-up":
        D['Name'] = get_string("What is your name for pick-up? ")
    if user_input == "Delivery":
        D['Cost'] += 3
        D['Name'] = get_string("What is you name for delivery? ")
        D['Address'] = get_string("What is your address? ")
        D['Phone'] = get_integer("What is you phone number? ")
        print("-" * 60)
        print("Your cost is now ${}".format(D['Cost']))
        print("-" * 60)
    return D

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
        ["Q", "Quit"]
    ]

    delivery_pickup(customer_info)
    run_program = True
    while run_program:
        print("-" * 60)
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 60)
        user_choice = get_string("Please select an option: ")
        if user_choice == "P":
            print("=~" * 30)
            pizza_menu(pizza_types)
            print("=~" * 30)
        if user_choice == "Q":
            print("=~" * 30)
            print("Thank you, the program has ended")
            print("=~" * 30)
            run_program = False


if __name__ == "__main__":
    main()