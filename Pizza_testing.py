def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

def pizza_menu(l):
    for x in l:
        output = "{:<25} -- ${}".format(x[0], x[1])
        print(output)
    return None

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
        ["Q", "Quit"]
    ]

    delivery_pickup(customer_info)
#    print(customer_info)

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ")
        if user_choice == "P":
            pizza_menu(pizza_types)
        if user_choice == "Q":
            run_program = False

if __name__ == "__main__":
    main()