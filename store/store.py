""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def store_options():
    run_menu = True
    while run_menu == True:
        table = data_manager.get_table_from_file('store/games.csv')
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':  
            show_table(table)
            ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                          'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
        elif option == '2':
            add(table)

            ui.print_menu('Store',
                ['Show Table', 'Add new data to table', 'Remove data from table', 
                'Update table data','How many different kinds of game are available of each manufacturer?',
                'What is the average amount of games in stock of a given manufacturer?'],
                'Return To Main Menu', )
        elif option == '3':
            get_id = ui.get_inputs(['Enter the id you want to remove: '], '')
            remove(table, get_id)

            ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                         'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
        elif option == '4':
            get_id = ui.get_inputs(['Enter the id you want to update: '], '')
            update(table, get_id)

            ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                         'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
        elif option == '5':
            value = convert_to_list(get_counts_by_manufacturers(table))
            labels = ['Manufacturer', 'Number of games']
            ui.print_table(value, labels)

            ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                         'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
        elif option == '6':
            get_manufacturer = ui.get_inputs(['Enter manufacturer: '], '')
            result = get_average_by_manufacturer(table, get_manufacturer)
            ui.print_result(result,f'Average stock by manufacturer {get_manufacturer[0]} is ')

            ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                         'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
            
        elif option == '0':
            run_menu = False
        else:
            raise KeyError("There is no such option.")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.
    Returns:
        None
    """

    ui.print_menu('Store',
                         ['Show Table', 'Add new data to table', 'Remove data from table', 
                         'Update table data','How many different kinds of game are available of each manufacturer?',
                         'What is the average amount of games in stock of a given manufacturer?'],
                         'Return To Main Menu', )
    store_options()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    item = ui.get_inputs(['title: ', 'manufacturer: ', 'price: ', 'in_stock: '], 'Enter game')
    id = common.generate_random(table)
    item.insert(0, id)
    table.append(item)
    data_manager.write_table_to_file('store/games.csv', table)
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

    new_table = common.remove_from_list(table, id_)
    data_manager.write_table_to_file('store/games.csv', new_table)
    return new_table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    list_labels = ['new id: ', 'new title: ', 'new manufacturer: ', 'new price: ', 'new stock: ']
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            item = ui.get_inputs(list_labels, ' Enter')
            table.pop(i)
            table.insert(i, item)
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    MANUFACTURER = 2
    games_amount = {}
    all_manufacturers = [table[i][MANUFACTURER] for i in range(len(table))]
    unique = set(all_manufacturers)
    for unique_manufacturer in unique:
        counter = 0
        for manufacturer in all_manufacturers:
            if unique_manufacturer == manufacturer:
                counter +=1
        games_amount[unique_manufacturer] = counter
    return games_amount


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    MANUFACTURERS = 2
    GAMES_IN_STOCK = 4
    stock = 0
    number_of_games_manufacturer = 0 
    split_strings = manufacturer[0].split(' ')
    capitalized_manufacturer = [values.capitalize() for values in split_strings]
    for data in table:
        for string in capitalized_manufacturer:
            if ' '.join(capitalized_manufacturer) == data[MANUFACTURERS]:
                number_of_games_manufacturer +=1 
                stock += int(data[GAMES_IN_STOCK])
    try:
        return stock // number_of_games_manufacturer
    except ZeroDivisionError:
        return 0

def convert_to_list(dictionary):
    list = [[key,str(value)] for key,value in dictionary.items()]
    return list

