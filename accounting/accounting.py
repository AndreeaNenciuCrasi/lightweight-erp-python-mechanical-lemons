""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'),
        2 number, 2 lower and 2 upper case letters)
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
                ui.print_error_message('Invalid command. Please choose between'
                                       ' 0 and 6.')
        option = inputs[0]
        table = data_manager.get_table_from_file('accounting/items.csv')
        if option == '1':
            show_table(table)
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
        elif option == '2':
            add(table)
            data_manager.write_table_to_file('accounting/items.csv', table)
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
        elif option == '3':
            remove_id_ = ui.get_inputs(['Please enter the ID of the item'
                                        ' to remove: '], 'Accounting -')[0]
            table = remove(table, remove_id_)
            data_manager.write_table_to_file('accounting/items.csv', table)
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
        elif option == '4':
            update_id_ = ui.get_inputs(['Please enter the ID of the item'
                                        ' to update: '], 'Accounting -')[0]
            update(table, update_id_)
            data_manager.write_table_to_file('accounting/items.csv', table)
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
        elif option == '5':
            highest_profit = which_year_max(table)
            ui.print_result(highest_profit, 'Accounting data - '
                                            'The most profitable year is ')
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
        elif option == '6':
            year = int(ui.get_inputs(['Please enter the year to calculate'
                                      ' the average profit/game for: '],
                                     'Accounting -')[0])
            average = avg_amount(table, year)
            ui.print_result(average, 'Accounting data - average profit per'
                            f' game sold in {year}: ')
            ui.print_menu('Accounting', ['Show table', 'Add', 'Remove',
                          'Update', 'Most profitable year', 'Average profit/game'],
                          'Return to main menu')
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

    ui.print_menu('Accounting', ['Show table', 'Add', 'Remove', 'Update',
                  'Most profitable year', 'Average profit/game'], 'Return to'
                  ' main menu')
    choose_accounting()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ['ID', 'month', 'day', 'year', 'type', 'amount'])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    item = ui.get_inputs(['month: ', 'day: ', 'year: ', 'type: ', 'amount: '],
                         'Add transaction -')
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

    list_labels = ['ID: ', 'month: ', 'day: ', 'year: ', 'type: ', 'amount: ']
    for i in range(len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, 'Accounting -')
            table.pop(i)
            table.insert(i, item)
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

    years = []
    for game in table:
        if game[3] not in years:
            years.append([game[3], 0])
    for game in table:
        if game[4] == 'in':
            i = 0
            for i in range(len(years)):
                if game[3] == years[i][0]:
                    years[i][1] += int(game[5])
        elif game[4] == 'out':
            for j in range(len(years)):
                if game[3] == years[j][0]:
                    years[j][1] -= int(game[5])
    most_profits = ['no data', 0]
    for year in years:
        if year[1] > most_profits[1]:
            most_profits = year
    return int(most_profits[0])


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year?
    [(profit)/(items count)]
    Each line in the accounting table represents a game
    (in = sold, out = bought).
    items_count represents all games bought and sold in the given year.

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    profit = 0
    items_count = 0
    for item in table:
        if int(item[3]) == year:
            if item[4] == 'in':
                profit += int(item[5])
                items_count += 1
            elif item[4] == 'out':
                profit -= int(item[5])
                items_count += 1
    avg = profit/items_count
    return avg


def average_monthly_in(year_in, year_out):
    """
    Calculates how much customers spend per month at the store.
    This function is used in the data analyser module to compare to
    the average monthly game prices to see the correlation between game
    prices and customer purchasing power. This is a rough simulation of
    data science in the customer_keep_up_purchasing_power() function.
    Args:
        year_in and year_out, int
    Returns:
        list of int (average for each month in the range)
    """

    table = data_manager.get_table_from_file('accounting/items.csv')
    monthly_avg_ins = []
    for year in range(year_in, year_out + 1):
        for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            month_total_ins = []
            for i in table:
                if i[3] == str(year) and i[1] == str(month) and i[4] == 'in':
                    month_total_ins.append(int(i[5]))
            monthly_avg_ins.append(common.mean(month_total_ins))
    return monthly_avg_ins
