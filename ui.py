""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    TABLE_SPACING_IN_CELL = 5
    rows = len(table) + 1  # title_list counts as one row
    columns = len(title_list)
    column_widths = [[i, len(title_list[i])] for i in range(len(title_list))]
    for i in range(columns):
        for line in table:
            if len(line[i]) > column_widths[i][1]:
                column_widths[i][1] = len(line[i])
    table.insert(0, title_list)
    total_width = 0
    for j in column_widths:
        total_width += j[1] + TABLE_SPACING_IN_CELL
    print('/'+'-' * (total_width - 2)+'\\')
    for item in table:
        for i in range(columns):
            if i != columns - 1:
                wide = column_widths[i][1] + TABLE_SPACING_IN_CELL
                print('|' + item[i].center(wide-1), end='')
            elif i == columns - 1:
                wide = column_widths[i][1] + TABLE_SPACING_IN_CELL - 1
                print('|' + item[i].center(wide-1), end='')
        if item != table[-1]:
            print('|', end='')
            print('\n'+'|'+'-' * (total_width - 2)+'|')
        elif item == table[-1]:
            print('|', end='')
            print('\n'+'\\'+'-' * (total_width - 2)+'/')


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'{label}{result}')  # the label must come from the function, ex: "Accounting data - most profitable year"


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'    {title}')
    i = 1
    while i <= len(list_options):
        print(f'        ({i}) {list_options[i-1]}')
        i += 1
    print(f'        (0) {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    i = 0
    inputs = []
    while i < len(list_labels):
        inputs.append(input(f'{title} {list_labels[i]}'))
   
   #  print(f'{title}')
   #  while i < len(list_labels):
   #      inputs.append(input(f'{list_labels[i]}'))

        i += 1
    
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'Error - {message}')
