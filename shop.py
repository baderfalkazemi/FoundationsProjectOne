####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "codedcupcakes"
signature_flavors = ["nutella", "kinder", "oreo", "lotus"]
order_list = []

master_menu = {
    "vanilla": 2,
    "chocolate": 2,
    "strawberry": 2,
    "caramel": 2,
    "rasberry": 2,
    "nutella": 2.750,
    "kinder": 2.750,
    "oreo": 2.750,
    "lotus": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}

def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our Menu: ")
    for item in menu:
        print('- "%s" (%s KD)' % (item, menu[item]))


def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print('- "%s"' % item)


def print_signatures():
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print('- "%s"' % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order.lower() in menu:
        return True
    elif order.lower() in original_flavors:
        return True
    elif order.lower() in signature_flavors:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = input("What's your order? Order with correct spelling and type 'exit' when you're ready to checkout. ").lower()
    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return True
    else:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for pricing in order_list:
        for prices in master_menu:
            if pricing == prices:
                total = total + master_menu[prices]

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print(order_list)
    total = get_total_price(order_list)
    print("The total price of your order is %s KD." % total)
    if accept_credit_card == True:
        print("You can pay by cash or credit card.")
    else:
        print("please pay by cash, since we can't accept credit cards for any order of less than 5 KD.")
    print()
    print("Thanks for visiting %s today. Please come back again. Thank you!" % cupcake_shop_name)