def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

global cost
cost = 0

def pizza_menu(l):
    for x in l:
        output = "{:<25} -- ${}".format(x[0], x[1])
        print(output)
    return None






def main():
    cost = 3

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