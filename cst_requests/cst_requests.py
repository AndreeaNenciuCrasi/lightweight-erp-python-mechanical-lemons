""" Customer games cst_requests module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game requested
    * developer (string): Name of the developing company
    * year (number): Year when the customer placed the request
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose_requests():
    requests_menu_active = True
    while requests_menu_active is True:
        valid_command = False
        while valid_command is False:
            try:
                inputs = ui.get_inputs(["Please enter a number: "], "")
                if inputs[0].isdigit() is False:
                    raise ValueError
                if int(inputs[0]) in range(0, 7):
                    valid_command = True
                elif inputs[0] not in range(0, 7):
                    raise ValueError
            except ValueError:
                ui.print_error_message('Invalid command. Please choose between 0 and 6.')
        option = inputs[0]
        table = data_manager.get_table_from_file('cst_requests/cst_requests.csv')
        if option == '1':
            show_table(table)
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '2':
            add(table)
            data_manager.write_table_to_file('cst_requests/cst_requests.csv', table)
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '3':
            remove_id_ = ui.get_inputs(['ID of item to remove: '], 'Requests')[0]
            remove(table, remove_id_)
            data_manager.write_table_to_file('cst_requests/cst_requests.csv', table)
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '4':
            update_id_ = ui.get_inputs(['ID of item to update: '], 'Requests')[0]
            update(table, update_id_)
            data_manager.write_table_to_file('cst_requests/cst_requests.csv', table)
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '5':
            most_requested_list = most_requested(table)
            ui.print_table(most_requested_list, ['id', 'title', 'developer', 'year of request'])
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '6':
            oldest_requested_game = oldest_request(table)
            ui.print_table(oldest_requested_game, ['id', 'title', 'developer', 'year of request'])
            ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
        elif option == '0':
            requests_menu_active = False


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    ui.print_menu('Requests', ['Show table', 'Add', 'Remove', 'Update',
                  'Most requested game', 'Oldest requested game'], 'Return'
                  ' to main menu')
    choose_requests()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ['id', 'title', 'developer', 'year of request'])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    item = ui.get_inputs(['title: ', 'developer: ', 'year of request: '], 'Add customer game request -')
    id = common.generate_random(table)
    item.insert(0, id)
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
    for i in range(len(table)):
        if table[i][0] == id_:
            table.pop(i)
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
    list_labels = ['id', 'title', 'developer', 'year of request']
    for i in range(len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, 'Customer game request')
            table.pop(i)
            table.insert(i, item)
    return table


# special functions:
# ------------------


def most_requested(table):
    """
    Question: What is the most requested game by customers? [the game title
    that shows up the most in the table]

    Args:
        table (list): data table to work on

    Returns:
        list of info for the title, or if more than one, all the titles of the games, as a table
    """
    titles_list = []
    for line in table:
        titles_list.append(line[1])
    most_apearances = 0
    most_frequent = []
    for title in titles_list:
        if common.how_many_times(titles_list, title) > most_apearances:
            most_frequent = []
            most_frequent.append(title)
            most_apearances = common.how_many_times(titles_list, title)
        elif common.how_many_times(titles_list, title) == most_apearances:
            most_frequent.append(title)
    final_list = []
    for game in table:
        if game[1] in most_frequent and game[1] not in [i[1] for i in final_list]:
            final_list.append(game)
    return final_list


def oldest_request(table):
    """
    Question: What is the oldest request a customer has made? [the table item
    with the oldest year of request]

    Args:
        table (list): data table to work on

    Returns:
        list of info for the title, or if more than one, all the titles of the
        games, as a table
    """
    table = common.bubbleSort(table, 3)
    oldest_year = table[0][3]
    oldest_requested_games = []
    for game in table:
        if game[3] == oldest_year:
            oldest_requested_games.append(game)
    return oldest_requested_games
