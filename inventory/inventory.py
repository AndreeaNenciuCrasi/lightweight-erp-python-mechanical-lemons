""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def choose_inventory():
    inventory_menu_active = True
    while inventory_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file('inventory/inventory.csv')
        if option == '1':
            show_table(table)
        elif option == '2':
            add(table)
            data_manager.write_table_to_file('inventory/inventory.csv', table)
        elif option == '3':
            id_ = ui.get_inputs(['ID of item to remove: '], 'Inventory')[0]
            remove(table, id_)
            data_manager.write_table_to_file('inventory/inventory.csv', table)
        elif option == '4':
            id_ = ui.get_inputs(['ID of item to update: '], 'Inventory')[0]
            update(table, id_)
            data_manager.write_table_to_file('inventory/inventory.csv', table)
        elif option == '5':
            year = int(ui.get_inputs(['Year to calculate availability: '], 'Inventory')[0])
            available_item = get_available_items(table,year)
            #ui.print_result(available_item, f'Inventory data - items that have not exceeded their durability yet (in {year}): ')
        elif option == '6':
            average = get_average_durability_by_manufacturers(table)
            get_average_durability_by_manufacturers(table)
            ui.print_result(average,'Inventory data - the average durability times for each manufacturer: ')
        elif option == '0':
            inventory_menu_active = False

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    #table = data_manager.get_table_from_file("inventory/inventory.csv")
    ui.print_menu('Inventory', ['Show table', 'Add', 'Remove', 'Update', 'Which items have not exceeded their durability yet?', 'What are the average durability times for each manufacturer?'], 'Return to main menu')
    choose_inventory()
    


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    ui.print_table(table, ['id', 'name', 'manufacturer', 'purchase_year', 'durability'])
    
   


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    #table = data_manager.get_table_from_file("inventory/inventory.csv")
    item = ui.get_inputs(['Id: ', 'Name: ', 'Manufacturer: ', 'Purchase year: ', 'Durability: '], 'Please provide product data: ')
    table.append(item)
    ui.print_table(table, ['id', 'name', 'manufacturer', 'purchase_year', 'durability'])
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

    for i in range(len(table)):
        if table[i][0] == id_:
            table.pop(i)
    ui.print_table(table, ['id', 'name', 'manufacturer', 'purchase_year', 'durability'])
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

    list_labels = ['id: ', 'name: ', 'manufacturer: ', 'purchase_year: ', 'durability: ']
    for i in range(len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, 'Inventory')
            table.pop(i)
            table.insert(i, item)
    ui.print_table(table, ['id', 'name', 'manufacturer', 'purchase_year', 'durability'])
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    expiration = []
    for i in range(len(table)):
        expiration_date = int(table[i][3])+int(table[i][4])
        if year < expiration_date:
            expiration.append(table[i])
    ui.print_table(expiration, ['id', 'name', 'manufacturer', 'purchase_year', 'durability'])
    return expiration


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """




            
   
