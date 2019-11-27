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
    * customer_id (string): id from the crm
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
CUSTOMER_ID = 6


def choose_sales(sales_menu_list):
    sales_menu_active = True
    table = data_manager.get_table_from_file('sales/sales.csv')
    while sales_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            show_table(table)
            ui.print_menu('Sales manager', sales_menu_list,
                          'Return to main menu')
        elif option == '2':
            add(table)
            ui.print_menu('Sales manager', sales_menu_list,
                          'Return to main menu')
        elif option == '3':
            id = ui.getinputs(['Record to be deleted: '], '')[0]
            remove(table, id)
            data_manager.write_table_to_file('sales/sales.csv', table)
            ui.print_menu('Sales manager', sales_menu_list,
                          'Return to main menu')
        elif option == '4':
            id = ui.getinputs(['Record to be updated: '], '')[0]
            update(table, id)
            data_manager.write_table_to_file('sales/sales.csv', table)
            ui.print_menu('Sales manager', sales_menu_list,
                          'Return to main menu')
        elif option == '5':
            lowest_price = get_lowest_price_item_id(table)
            ui.print_result(lowest_price, 'Product ID with lowest price: ')
            ui.print_menu('Sales manager', sales_menu_list,
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
            ui.print_menu('Sales manager', sales_menu_list,
                          'Return to main menu')
        elif option == '7':
            id_ = ui.get_inputs(['Please input the sale ID: '], '')[0]
            ui.print_result(get_title_by_id(id_), f' The title of sale {id_} is: ')
        elif option == '8':
            id_ = ui.get_inputs(['Please input the sale ID: '], '')[0]
            ui.print_result(get_title_by_id_from_table(table, id_), f' The title of sale {id_} is: ')
        
        elif option == '14':
            id_ = ui.get_inputs(['Please input sale id: '], '')[0]
            ui.print_result(get_customer_id_by_sale_id(id_), f'The customer id, from sale id {id_} is: ')
        elif option == '15':
            id_ = ui.get_inputs(['Please input sale id: '], '')[0]
            ui.print_result(get_customer_id_by_sale_id_from_table(table, id_), f'The customer id, from table sale id {id_} is: ')
        elif option == '16':
            ui.print_result(get_all_customer_ids(), f'All sales customer ids: ')
        elif option == '17':
            ui.print_result(get_all_customer_ids_from_table(table), f'All table sales customer ids: ')
        elif option == '18':
            ui.print_result(get_all_sales_ids_for_customer_ids(), f'All sales ids for customer ids: ')
        elif option == '19':
            ui.print_result(get_all_sales_ids_for_customer_ids_from_table(table), f'All sales ids for customer ids: ')
        elif option == '20':
            ui.print_table(get_num_of_sales_per_customer_ids(), ['customer id', 'sales'])
        elif option == '21':
            ui.print_table(get_num_of_sales_per_customer_ids_from_table(table), ['customer id', 'sales'])
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

    sales_menu_list = ['Show table', 'Add', 'Remove',
                  'Update', 'Lowest price item', 'Items sold between', 
                  'DA title by id', 'DA title by id from table', 
                  'DA item id sold last', 'DA item id sold last from table', 
                  'DA item title sold last from table', 'DA sum of prices', 
                  'DA sum of prices from table', 'DA _d customer id by sale id', 
                  'DA customer id by sale id from table', 'DA all customer ids', 
                  'DA all customer ids from table', 'DA all sales ids for cst ids', 
                  'DA all sales ids for cst ids from table', 'DA num of sales per cst ids', 
                  'DA num sales per cst id from table']
    ui.print_menu('Sales manager', sales_menu_list, 'Return to main menu')
    choose_sales(sales_menu_list)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    titles = ['id', 'title', 'price', 'month', 'day', 'year', 'customer id']
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

    # your code


# functions supports data analyser
# --------------------------------


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    TITLE = 1
    ID = 0
    table = data_manager.get_table_from_file('sales/sales.csv')
    for data in table:
        if data[ID] == id:
            return data[TITLE]
    return None


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    TITLE = 1
    ID = 0
    for data in table:
        if data[ID] == id:
            return data[TITLE]
    return None


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    sale_dates_list = []
    sale_date = 0
    for line in table:
        sale_date = common.calculate_days(
            line[YEAR + 1], line[MONTH + 1], line[DAY + 1])
        sale_dates_list.append((line[0], sale_date))
    latest_date = max(sale_dates_list, key=lambda key: sale_dates_list[1])
    return latest_date[0]



def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    sale_dates_list = []
    sale_date = 0
    for line in table:
        sale_date = common.calculate_days(
            line[YEAR + 1], line[MONTH + 1], line[DAY + 1])
        sale_dates_list.append((line[0], sale_date))
    latest_date = max(sale_dates_list, key=lambda key: sale_dates_list[1])
    return latest_date[0]

def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    sale_dates_list = []
    sale_date = 0
    for line in table:
        sale_date = common.calculate_days(
            line[YEAR + 1], line[MONTH + 1], line[DAY + 1])
        sale_dates_list.append((line[TITLE+1], sale_date))
    latest_date = max(sale_dates_list, key=lambda key: sale_dates_list[1])
    return latest_date[0]


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    table = data_manager.get_table_from_file('sales/sales.csv')

    sum = 0
    for line in table:
        for element in item_ids:
            if line[0] == element:
                sum += int(line[PRICE+1])
    return sum


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    sum = 0
    for line in table:
        for element in item_ids:
            if line[0] == element:
                sum += int(line[PRICE+1])
    return sum


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    for i in table:
        if i[0] == sale_id:
            return i[-1]
    return None


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    for i in table:
        if i[0] == sale_id:
            return i[-1]
    return None


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    customer_ids = set()
    for i in table:
        customer_ids.add(i[-1])
    return customer_ids


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    customer_ids = set()
    for i in table:
        customer_ids.add(i[-1])
    return customer_ids


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    id_dictionary = {}
    for line in table:
        customer = line[-1]
        if customer not in id_dictionary:
            id_dictionary[customer] = [line[0]]
        elif customer in id_dictionary:
            id_dictionary[customer].append(line[0])
    return id_dictionary


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    id_dictionary = {}
    for line in table:
        customer = line[-1]
        if customer not in id_dictionary:
            id_dictionary[customer] = [line[0]]
        elif customer in id_dictionary:
            id_dictionary[customer].append(line[0])
    return id_dictionary


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    dict_cust_ID_number_of_sales = {}
    for i in table:
        customer = i[-1]
        if customer not in dict_cust_ID_number_of_sales:
            dict_cust_ID_number_of_sales[customer] = 1
        elif customer in dict_cust_ID_number_of_sales:
            dict_cust_ID_number_of_sales[customer] += 1
    return dict_cust_ID_number_of_sales


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    dict_cust_ID_number_of_sales = {}
    for i in table:
        customer = i[-1]
        if customer not in dict_cust_ID_number_of_sales:
            dict_cust_ID_number_of_sales[customer] = 1
        elif customer in dict_cust_ID_number_of_sales:
            dict_cust_ID_number_of_sales[customer] += 1
    return dict_cust_ID_number_of_sales
