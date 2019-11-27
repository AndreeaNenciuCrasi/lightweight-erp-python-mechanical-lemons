"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def choose_data_analyser(data_analyser_menu_list):
    data_analyser_menu_active = True
    while data_analyser_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            get_the_last_buyer_name()
        elif option == '2':
            get_the_last_buyer_id()
        elif option == '3':
            get_the_buyer_name_spent_most_and_the_money_spent()
        elif option == '4':
            get_the_buyer_id_spent_most_and_the_money_spent()
        elif option == '5':
            get_the_most_frequent_buyers_names(num=1)
        elif option == '6':
            frequent_buyers_number = int(ui.get_inputs(['frequent buyers you want to see: '], 'Please input the number of top ')[0])
            ui.print_result(get_the_most_frequent_buyers_ids(frequent_buyers_number), 'Most frequent buyer(s) id(s), and number of sales: ')
        elif option == '0':
            data_analyser_menu_active = False


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    data_analyser_menu_list = ["Last buyer's name", "Last buyer's ID", "The buyer that spent the most and how much", "The buyer ID that spent the most and how much", "The most frequent buyers' names", "The most frequent buyers' IDs"]
    ui.print_menu('Data analyser', data_analyser_menu_list, 'Return to main menu')
    choose_data_analyser(data_analyser_menu_list)


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # list of cust id and how many sales each

    # list name/ID
    # for i in range(num) result.append(name/sales)


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    working_dictionary = sales.get_num_of_sales_per_customer_ids()
    customer_ID_sales_amount = []
    for key, value in working_dictionary.items():
        customer_ID_sales_amount.append((key, value))
    result = []
    i = 0
    while i < num:
        result.append(customer_ID_sales_amount[i])
        i += 1
    return result
