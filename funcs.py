# Coded by Jayquon Coblentz
# Version 4.5.1


from fractions import Fraction

import python_calamine


treated = []
untreated = []
material_types = []
cutlist_name = ""
file_loads = 0


def excel_calamine(file: bytes):
    global cutlist_name
    workbook = python_calamine.CalamineWorkbook.from_filelike(file)
    rows = iter(workbook.get_sheet_by_index(0).to_python())
    cutlist_name = list(map(str, next(rows)))[0]
    for row in rows:
        yield row


def open_xlsx(filename):
    global treated
    global untreated
    global material_types
    global cutlist_name
    global file_loads

    tmp_list = []

    # Check for previous loads
    if file_loads > 0:
        treated = []
        untreated = []
        material_types = []

    # Load xlsx file into tmp_list
    with open(filename, 'rb') as f:
        rows = excel_calamine(f)
        for row in rows:
            tmp_list.append(row)

    # Populate treated and untreated lists from tmp_list while removing from tmp_list as you go
    for i in range(2):
        list_type = [treated, untreated]
        keyword = ["treated", "untreated"]
        current_list = 0  # Set default first list to 0 (treated)

        if len(tmp_list) == 0:  # End of tmp_list check
            break

        while tmp_list[0][0].strip().lower() not in keyword:  # Find begining of list
            tmp_list.pop(0)
            if len(tmp_list) == 0:  # End of tmp_list check
                break

        if len(tmp_list) == 0:  # End of tmp_list check
            break

        if tmp_list[0][0].strip().lower() == keyword[1]:  # If untreated found first, change list to add to
            current_list = 1

        tmp_list.pop(0)

        while type(tmp_list[0][1]) is float:  # Populate list
            list_type[current_list].append([tmp_list[0][1], tmp_list[0][2], tmp_list[0][4]])
            tmp_list.pop(0)
            if len(tmp_list) == 0:  # End of tmp_list check
                break

    prep_lists(treated)
    prep_lists(untreated)
    file_loads += 1
    return cutlist_name


def prep_lists(list):
    # Prep list
    for row in list:
        row[0] = int(row[0])
        row[1] = row[1].strip()
        length = row[2]

        if type(length) is str:

            # Process length for convert to int
            length = length.strip()
            length = length.strip('"')
            length = length.split()

            if length[0].isdigit():  # Check for fraction
                if len(length) == 2:
                    row[2] = int(length[0]) + float(Fraction(length[1]))
                elif len(length) == 1:
                    row[2] = int(length[0])
        else:
            row[2] = length


def get_types():
    # Populate list of materials from cutlist
    for cutlist in [treated, untreated]:
        for row in cutlist:
            if row[1] in material_types:
                pass
            else:
                material_types.append(row[1])

    return material_types


def stock_calc(stock_len, board_type, qty):
    # Let user select from list of materials in cutlist
    treated_stock_used = 0
    untreated_stock_used = 0
    stock_used = [treated_stock_used, untreated_stock_used]

    if board_type not in material_types:
        return "Invalid Type Selection"

    stock_len = stock_len.strip()
    if stock_len.isdigit():
        stock_len = float(stock_len)
    else:
        return "Invalid stock length input"

    # Find total boards required
    leftovers = []

    cutlist = [treated, untreated]

    for i in range(2):
        for board in cutlist[i]:
            is_long_enough = True
            if board[1] == board_type:
                board_length = board[2]
                board_quantity = board[0]
                # Make sure stock length is long enough for cutlist
                if board_length > stock_len:
                    frac = Fraction(board_length - int(board_length))
                    trail = ""
                    if frac:
                        trail = '-' + str(frac)
                    print(f'Stock length not long enough to complete cutlist. \nPlease use at least {int(board_length)}{trail}" material.')
                    is_long_enough = False

                if is_long_enough:
                    for j in range(board_quantity * qty):
                        # Check for peice in leftovers to satisfy
                        leftover = 0
                        leftovers.sort()
                        for peice in leftovers:
                            if board_length <= peice:
                                leftover = peice - board_length
                                leftovers.remove(peice)
                                break
                        else:
                            stock_used[i] += 1
                            leftover = stock_len - board_length

                        if leftover > 5:
                            leftovers.append(leftover)

    return stock_used
