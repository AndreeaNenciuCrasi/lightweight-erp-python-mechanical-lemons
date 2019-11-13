""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

NAME = 0
BIRTH_YEAR = 1


def choose_sales():
    sales_menu_active = True
    table = data_manager.get_table_from_file('hr/persons.csv')

    while sales_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            show_table(table)
        elif option == '2':
            add(table)
        elif option == '3':
            id_ = ui.get_inputs(['Record to be deleted: '], '')[0]
            remove(table, id_)
            data_manager.write_table_to_file('hr/persons.csv', table)
        elif option == '4':
            id_ = ui.get_inputs(['Record to be updated: '], '')[0]
            update(table, id_)
            data_manager.write_table_to_file('hr/persons.csv', table)
        elif option == '5':
            oldest = get_oldest_person(table)
            ui.print_result(oldest, 'Oldest person is: ')
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

    ui.print_menu('Human resources manager', ['Show table', 'Add', 'Remove', 'Update',
                                              'Oldest person', 'Persons closest to average'], 'Return to main menu')
    choose_sales()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ['id', 'name', 'birth_year']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    item = ui.get_inputs(['Please provide name: ', 'Please provide birth year: '],
                         'Please provide persons data:')
    table_csv = data_manager.get_table_from_file('hr/persons.csv')
    table.append([common.generate_random(table_csv),
                  item[NAME], item[BIRTH_YEAR]])
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

    list_labels = ['Please provide id: ',
                   'Please provide name: ', 'Please provide birth year: ']
    for i in range(1, len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, '')
            table.pop(i)
            table.insert(i, item)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    return_list = []
    person_list = common.bubbleSort(table, 2)
    for line in person_list:
        if person_list[0][2] == line[2]:
            return_list.append(line[1])
    return return_list


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
