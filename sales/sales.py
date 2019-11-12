""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose_sales():
    sales_menu_active = True
    table = data_manager.get_table_from_file('sales/sales.csv')
    while sales_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            show_table(table)
        elif option == '2':
            add(table)
        elif option == '3':
            remove(table, id_)
        elif option == '4':
            update(table, id_)
        elif option == '5':
            print('Under construction...')
        elif option == '6':
            print('Under construction 2...')
        elif option == '0':
            sales_menu_active = False


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove', 'Update',
                                    'Lowest price item', 'Items sold between'], 'Return to main menu')
    choose_sales()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    titles = ['id', 'title', 'price', 'month', 'day', 'year']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    item = ui.get_inputs(['Please provide month: ', 'Please provide day: ',
                          'Please provide year: ',
                          'Please provide type: ', 'Please provide amount: '],
                         'Please provide product data:')

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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
