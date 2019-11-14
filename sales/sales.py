""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'),
        2 number, 2 lower and 2 upper case letters)
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


TITLE = 0
PRICE = 1
MONTH = 2
DAY = 3
YEAR = 4


def choose_sales():
    sales_menu_active = True
    table = data_manager.get_table_from_file('sales/sales.csv')
    while sales_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            show_table(table)
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
        elif option == '2':
            add(table)
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
        elif option == '3':
            id_ = ui.get_inputs(['Record to be deleted: '], '')[0]
            remove(table, id_)
            data_manager.write_table_to_file('sales/sales.csv', table)
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
        elif option == '4':
            id_ = ui.get_inputs(['Record to be updated: '], '')[0]
            update(table, id_)
            data_manager.write_table_to_file('sales/sales.csv', table)
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
        elif option == '5':
            lowest_price = get_lowest_price_item_id(table)
            ui.print_result(lowest_price, 'Product ID with lowest price: ')
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
        elif option == '6':
            date_from = ui.get_inputs(['Please provide month from: ',
                                      'Please provide day from: ',
                                       'Please provide year from: '], '')
            month_from = date_from[0]
            day_from = date_from[1]
            year_from = date_from[2]
            date_to = ui.get_inputs(['Please provide month to: ',
                                    'Please provide day to: ',
                                     'Please provide year to: '], '')
            month_to = date_to[0]
            day_to = date_to[1]
            year_to = date_to[2]
            time_period = get_items_sold_between(table, month_from, day_from,
                                                 year_from, month_to, day_to,
                                                 year_to)
            for line in time_period:
                line[2] = str(line[2])
                line[3] = str(line[3])
                line[4] = str(line[4])
                line[5] = str(line[5])
            titles = ['id', 'title', 'price', 'month', 'day', 'year']
            ui.print_table(time_period, titles)
            ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                          'Update', 'Lowest price item', 'Items sold between'],
                          'Return to main menu')
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

    ui.print_menu('Sales manager', ['Show table', 'Add', 'Remove',
                  'Update', 'Lowest price item', 'Items sold between'],
                  'Return to main menu')
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

    item = ui.get_inputs(['title: ', 'price: ', 'sale month: ',
                          'sale day: ', 'sale year: '],
                         'Please provide product')
    table_csv = data_manager.get_table_from_file('sales/sales.csv')
    table.append([common.generate_random(table_csv), item[TITLE], item[PRICE],
                  item[MONTH], item[DAY], item[YEAR]])
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

    n = len(table)
    i = 0
    while i < n:
        temp = table[i][0]
        if temp == id_:
            table.pop(i)
        i += 1
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

    list_labels = ['Please provide id: ', 'Please provide title: ',
                   'Please provide price: ', 'Please provide month: ',
                   'Please provide day: ', 'Please provide year: ']
    for i in range(1, len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, '')
            table.pop(i)
            table.insert(i, item)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item
    by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    table = common.bubbleSort(table, 1)
    table = common.bubbleSort(table, 2)
    return table[0][0]


def get_items_sold_between(table, month_from, day_from, year_from,
                           month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates?
    (from_date < sale_date < to_date)

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

    days_from = common.calculate_days(year_from, month_from, day_from)
    days_to = common.calculate_days(year_to, month_to, day_to)
    product_list = []
    for line in table:
        yr, mo, dy = line[5], line[3], line[4]
        days = common.calculate_days(yr, mo, dy)
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])
        if days_from < days and days < days_to:
            product_list.append(line)
    return product_list
