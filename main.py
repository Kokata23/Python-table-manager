# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from datetime import datetime, timedelta

def define_matrix_parameters(matrix_length):
    rows = 1
    cols = 1
    aditional_cols = 0

    while rows * cols <= matrix_length:
        if rows + cols == matrix_length:
            break
        rows += 1
        cols += 1

        if rows >= 12:
            break

    if rows * cols > matrix_length:
        rows -= 1
        cols -= 1

    aditional_cols = matrix_length - rows * cols




    return rows, cols, aditional_cols




def create_matrix(rows, cols, aditional_cols):
    matrix = []
    counter = 1
    row = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append([counter, 'Free'])
            counter += 1
        matrix.append(row)

    if aditional_cols > 0:
        row = []
        for i in range(aditional_cols):
            row.append([counter, 'Free'])

            if len(row) >= cols:
                matrix.append(row)
                row = []
            counter += 1

        matrix.append(row)
    return matrix




def swap_values(table, value, pr_value):
    if table[1] == value:
        return pr_value

    return value



def change_table_status_in_matrix(matrix, table_number):
    # table_to_be_changed = None

    for rows in matrix:
        for c in rows:
            if c[0] == table_number:

                if c[1] == 'Booked':
                    print("You've entered a booked table, have your guests arrived?")
                    guests = input("Enter 'Yes' or 'No': ")
                    if guests.lower() == "no":
                        c[1] = swap_values(c, 'Booked', 'Free')
                        return matrix

                    elif guests.lower() == "yes":
                        c[1] = swap_values(c, 'Booked', 'Taken')
                        return matrix

                    else:
                        print("\x1b[31mIncorect input, try again\x1b[0m")
                        return matrix

                # if booked_tables_list:
                #     booked_tables_list.remove(c)

                c[1] = swap_values(c, 'Taken', 'Free')
                break

    return matrix



def booking_a_table(matrix, table_to_book):

    for rows in matrix:
        for c in rows:
            if c[0] == table_to_book:
                if c[1] == 'Booked':
                    print("\x1b[31mInvalid input. You can not book already booked table!!\x1b[0m")
                    return matrix

                if c[1] == 'Taken':
                    print("\x1b[31mInvalid input. You can not book already taken table!!\x1b[0m")
                    return matrix

                c[1] = swap_values(c, 'Free', 'Booked')

                break

    return matrix



def check_range_of_matrix(taken_table, matrix_length):
    if taken_table > matrix_length:
        return True

    return False


def sum_of_table_group(matrix, element_searching):
    counter = 0
    for r in matrix:
        for c in r:
            if c[1].lower() == element_searching.lower():
                counter += 1

    return counter



def create_live_hour(hour, minutes, *days):
    current_time = datetime.now()

    if not days:
        day = current_time.day
    else:
        day = days[0]

    if minutes >= 60:
        minutes -= 60
        hour += 1
        if hour >= 24:
            # TODO IF problem accure check here!!!
            hour = 23
            minutes = 59

            if not check_date(day):
                return None


    created_time = datetime(current_time.year, current_time.month, day, hour, minutes, 0)

    if created_time < current_time:
        return None

    return created_time


def create_booked_table(matrix, counter, name, hour, minutes, *days):

    for r in matrix:
        for c in r:
            if c[0] == counter:
                if days:
                    day = days[0]
                    if hour == 0:
                        minutes = 20
                    h = create_live_hour(hour, minutes, day)
                else:
                    h = create_live_hour(hour, minutes)

                if h:
                    table_booked_list = [c, name, h]
                    return table_booked_list

                return None



def from_book_to_free(matrix, table_to_book):
    for rows in matrix:
        for c in rows:

            if c[0] == table_to_book:
                c[1] = swap_values(c, 'Free', 'Booked')
                continue

    return matrix


def check_for_exparation_in_booked_tables(booked_tables_list, matrix):
    current_time = datetime.now()

    for t in booked_tables_list.copy():
        if t[-1] < current_time:
            matrix = from_book_to_free(matrix, t[0][0])
            booked_tables_list.remove(t)

        elif t[0][1].lower() == "taken" or t[0][1].lower() == "free":
            booked_tables_list.remove(t)

    return matrix


def check_date(date):
    # TODO Only the try block might be usefull from that function

    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    try:
        my_date = datetime(current_date.year, current_date.month, date)
    except ValueError:
        return None

    first_day_of_month = current_date.replace(day=1)

    if current_date.month == 12:
        last_day_of_month = current_date.replace(year=current_date.year + 1, month=1, day=1) - timedelta(days=1)
    else:
        last_day_of_month = current_date.replace(month=current_date.month + 1, day=1) - timedelta(days=1)

    if first_day_of_month <= my_date <= last_day_of_month:

        return date

    # return None


def check_for_waiting_booked_tables(waiting_to_be_booked_tables, booked_tables_list):
    current_time = datetime.now()

    for t in waiting_to_be_booked_tables.copy():
        if t[-1].day == current_time.day:
            t[0][1] = 'Booked'
            waiting_to_be_booked_tables.remove(t)
            is_in = [t for tb in booked_tables_list if tb[0][0] == t[0][0]]
            if not is_in:
                booked_tables_list.append(t)

        if t[-1].day < current_time.day:
            waiting_to_be_booked_tables.remove(t)


    # return waiting_to_be_booked_tables


def check_if_table_already_in(waiting_to_be_booked_tables, table_for_waiting_list):
    for t in waiting_to_be_booked_tables:
        if t[-1].day == table_for_waiting_list[-1].day and t[0][0] == table_for_waiting_list[0][0]:
            return True

    return False



def check_for_duplicates(table_to_be_removeds, table_date, table_name):
    table_for_removing = None

    for t in table_to_be_removeds:
        if table_name == t[1] and table_date == t[-1].day:
            table_for_removing = t
            return table_for_removing

    return table_for_removing



matrix_lenght = None

while True:
    try:
        matrix_lenght = int(input("Enter the number of tables your coffee/restaurant has: "))
    except ValueError:
        print("\x1b[31mIncorrect input, you have to enter an number!\x1b[0m")
        continue
    break

print()

rows, cols, aditional_cols = define_matrix_parameters(matrix_lenght)
matrix = create_matrix(rows, cols, aditional_cols)


for row in matrix:
    print('  |  '.join(f'{x[0]}-{x[1]}'for x in row))
    print()

booked_tables_list = []
waiting_to_be_booked_tables = []


while True:
    print("/ " * 25)
    print("\x1b[37mFor restarting, enter table number: '-1'\x1b[0m")
    print("\x1b[37mFor total count of tables state Enter: 'sum'\x1b[0m")
    print("\x1b[37mBooking for today, enter table number: '0'\x1b[0m")
    print("\x1b[37mTo see all tables booked for present date, Enter: 'booked'\x1b[0m ")
    print("\x1b[37mTo reserve a table, For future date, Enter '!'\x1b[0m ")
    print("\x1b[37mTo check all reservations, Not for today, Enter 'reserved'\x1b[0m ")
    print("\x1b[37mTo remove a reservation, Enter '-'\x1b[0m ")
    # print("\x1b[37mFor booking more than one table ,Enter: '+'\x1b[0m ")
    print("- " * 23)


    t_table = input("Enter table number/command: "
                    "\n")

# ______________________________________________________________________________________________________________________________

    if t_table.lower() == 'sum':
        table_group = input("Enter table state, free, booked or taken: ")
        if table_group.lower() not in ['free', 'booked', 'taken']:
            print("\x1b[31mIncorrect table state, must be 'free', 'booked' or 'taken', try again.\x1b[0m")
            print()
            continue
        table_count = sum_of_table_group(matrix, table_group)

        print(f"\x1b[32mWe have {table_count} {table_group} tables\x1b[0m")
        print()
        continue

# ______________________________________________________________________________________________________________________________

    if t_table.lower() == "booked":
        if booked_tables_list:
            print()
            for t in booked_tables_list:
                print(f"{t[0][0]}-{t[0][1]}-{t[1]}-{t[2]}\n"
                      f"{'- '* 20}")
            print()
        else:
            print("\x1b[30mNo booked tables yet\x1b[0m")
        continue

# ______________________________________________________________________________________________________________________________

    if t_table.lower() == "reserved":
        if waiting_to_be_booked_tables:
            print()
            for t in waiting_to_be_booked_tables:
                print(f"Table {t[0][0]} is reserved for {t[2]} by {t[1]}\n"
                      f"{'- '* 20}")
            print()
        else:
            print("\x1b[30mNo tables for reservation\x1b[0m")
        continue

# ______________________________________________________________________________________________________________________________

    if t_table.lower() == "-":
        if waiting_to_be_booked_tables:
            for t in waiting_to_be_booked_tables:
                print(f"Table {t[0][0]} is reserved for {t[2]} by {t[1]}\n"
                      f"{'- '* 20}")
            print()
        else:
            print("\x1b[30mNo reservations\x1b[0m")
            continue


        try:
            table_n = int(input('Enter one of the tables above: '))
        except ValueError:
            print("Table must be number")
            continue


        tables_to_be_removed = [x for x in waiting_to_be_booked_tables if x[0][0] == table_n]

        if len(tables_to_be_removed) > 1:
            print(f"There are more than one tables with {table_n} number")
            print("For more specifity...")
            table_date = int(input("Enter date: "))
            table_name = input("Enter name: ")

            final_table = check_for_duplicates(tables_to_be_removed, table_date, table_name)
            if not final_table:
                print("\x1b[31mNo table found with the given name and date, try again!\x1b[0m")
                continue
            else:
                waiting_to_be_booked_tables.remove(final_table)

        else:
            try:
                final_table = tables_to_be_removed[0]
            except IndexError:
                print("\x1b[31mNo tables with that number!\x1b[0m")
                print()
                continue

            waiting_to_be_booked_tables.remove(final_table)

        print(f"\x1b[32mTable {table_n} on the name of {final_table[1]} and date {final_table[2].day},"
              f" removed successfully :)\x1b[0m")
        continue


# ______________________________________________________________________________________________________________________________

    if t_table == '!':
        try:
            table_to_book = int(input('Enter tables booked number: '))
        except ValueError:
            print("\x1b[31mIncorrect input, booked table must be integer(number)!\x1b[0m")
            print()
            continue

        if check_range_of_matrix(table_to_book, matrix_lenght):
            print("\x1b[31mIncorrect input, booked table not in range!\x1b[0m")
            continue


        name_to_book_on = input("Enter name for reservation: ")
        if name_to_book_on.isdigit():
            print("\x1b[31mName must include letters\x1b[0m")
            continue


        try:
            date = int(input('Enter date of reservation: '))

        except ValueError:
            print("\x1b[31mIncorrect input, date must be integer(number)!\x1b[0m")
            print()
            continue

        date = check_date(date)

        if date is None:
            print("\x1b[31mDate must be withing the month, try again!\x1b[0m")
            print()
            continue

        try:
            hour_arraival = int(input('Enter hour arrival (0, 23): '))
            if hour_arraival > 23:
                print("\x1b[31mIncorrect hour arrival, must be between between 0 and 23, try again!\x1b[0m")
                print()
                continue
        except ValueError:
            print("\x1b[31mIncorrect input, hour arrival must be integer(number)!\x1b[0m")
            print()
            continue


        table_for_waiting_list = create_booked_table(matrix, table_to_book, name_to_book_on, hour_arraival, 0, date)

        if table_for_waiting_list:
            # TODO CHECK FOR TABLES IN THE LIST
            if check_if_table_already_in(waiting_to_be_booked_tables, table_for_waiting_list):
                print("\x1b[31mTable already reserved for the date!\x1b[0m")
            else:
                waiting_to_be_booked_tables.append(table_for_waiting_list)
                today = datetime.now()
                if table_for_waiting_list[-1].day != today.day:
                    print()
                    print("\x1b[32m---Table reserved successfully ;0\x1b[0m")

        else:
            print("\x1b[31mDate is eiter past or not in the current month, try again.\x1b[0m")
            continue


        if waiting_to_be_booked_tables:
            check_for_waiting_booked_tables(waiting_to_be_booked_tables, booked_tables_list)

        if booked_tables_list:
            matrix = check_for_exparation_in_booked_tables(booked_tables_list, matrix)

        print()

        for row in matrix:
            print('  |  '.join(f'{x[0]}-{x[1]}' for x in row))
            print()

        continue


# ______________________________________________________________________________________________________________________________


    try:
        taken_table = int(t_table)
    except ValueError:
        print("\x1b[31mIncorrect input, try again.\x1b[0m")
        print()
        continue


    if taken_table == -1:
        print("Program restarting...")
        matrix = create_matrix(rows, cols, aditional_cols)
        booked_tables_list = []
        waiting_to_be_booked_tables = []


    if check_range_of_matrix(taken_table, matrix_lenght):
        print("\x1b[31mTable not in range, try again.\x1b[0m")
        continue


# ______________________________________________________________________________________________________________________________

    if taken_table == 0:
        try:
            table_to_book = int(input('Enter tables booked number: '))
        except ValueError:
            print("\x1b[31mIncorrect input, booked table must be integer(number)!\x1b[0m")
            print()
            continue

        if check_range_of_matrix(table_to_book, matrix_lenght):
            print("\x1b[31mIncorrect input, booked table not in range!\x1b[0m")
            continue


        name_to_book_on = input("Enter name the table is booked on: ")
        if name_to_book_on.isdigit():
            print("\x1b[31mName must include letters\x1b[0m")
            continue


        try:
            hour_arraival = int(input('Enter hour arrival (0, 23): '))
            if hour_arraival > 23:
                print("\x1b[31mIncorrect hour arrival, must be between between 0 and 23, try again!\x1b[0m")
                print()
                continue
        except ValueError:
            print("\x1b[31mIncorrect input, hour arrival must be integer(number)!\x1b[0m")
            print()
            continue

        try:
            minutes = int(input("Enter minutes arrival between 0 and 60 (optional): ")) + 10
            if minutes > 70:
                print("\x1b[31mIncorrect minutes, can not be grater than 100!\x1b[0m ")
                print()
                continue

        except ValueError:
            minutes = 10

        print("Whether you've entered minutes, 10 were added, because people are always late ;)")


        table_for_booked_list = create_booked_table(matrix, table_to_book, name_to_book_on, hour_arraival, minutes)

        if table_for_booked_list:
            matrix = booking_a_table(matrix, table_to_book)
            booked_tables_list.append(table_for_booked_list)
# ______________________________________________________________________________________________________________________________


    else:
        matrix = change_table_status_in_matrix(matrix, taken_table)


    if waiting_to_be_booked_tables:
        check_for_waiting_booked_tables(waiting_to_be_booked_tables, booked_tables_list)

    if booked_tables_list:
        matrix = check_for_exparation_in_booked_tables(booked_tables_list, matrix)



    print()
# ______________________________________________________________________________________________________________________________

    for row in matrix:
        print('  |  '.join(f'{x[0]}-{x[1]}' for x in row))
        print()

    if waiting_to_be_booked_tables:
        print(f"\x1b[30mYou have\x1b[0m \x1b[37m{len(waiting_to_be_booked_tables)}\x1b[0m \x1b[30mreserved tables for next couple of days\x1b[0m")


