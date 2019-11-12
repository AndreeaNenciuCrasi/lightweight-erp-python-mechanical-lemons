""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose_accounting():
    accounting_menu_active = True
    while accounting_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            table = data_manager.get_table_from_file('accounting/items.csv')
            show_table(table)
        elif option == '2':
            table = data_manager.get_table_from_file('accounting/items.csv')
            add(table)
            data_manager.write_table_to_file('accounting/items.csv', table)
        elif option == '3':
            remove_table(table, id_)
        elif option == '4':
            update_table(table, id_)
        elif option == '5':
            print('Under construction...')
        elif option == '6':
            print('Under construction 2...')
        elif option == '0':
            accounting_menu_active = False


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    ui.print_menu('Accounting', ['Show table', 'Add', 'Remove', 'Update', 'Which year max?', 'Average amount'], 'Return to main menu')
    choose_accounting()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ['id', 'month', 'day', 'year', 'type', 'amount'])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    item = ui.get_inputs(['id', 'month', 'day', 'year', 'type', 'amount'], 'Please provide product data:')
    table.append(item)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    return 9000
    

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    return 9001
