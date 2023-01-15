#import required modules
from datetime import date

### MAIN FUNCTIONS ###

# admin to add a new user with new username and password
def reg_user(usernames):
    '''adds new username and password to register user'''
    if user_name != 'admin':
        print("-----------------------------------")
        print("Registering new users requires admin privileges")
        print("-----------------------------------")
        return

    while True:
        new_user_name = input("Please enter a new username: ")
        new_pass_word = input("Please enter a new password: ")

        # print message to try again if username already taken
        if new_user_name in usernames:
            print("-----------------------------------")
            print("This username is taken, please try again")
            print("-----------------------------------")

        # write new username/password to user.txt file
        elif new_user_name not in usernames:
            with open("user.txt", "a") as file:
                file.write(f"\n{new_user_name}, {new_pass_word}")
                print("-----------------------------------")
                print("New user added!")
                print("-----------------------------------")
                return

# ask user to input date and convert to string
def get_date_from_user_and_return_saved_date_string(user_message):
    '''gets date from user and returns date string in format dd mmm yyyy'''
    while True:
        try:
            date_string = input(user_message)
            date_variable = convert_string_to_datetime_date(date_string)
            date_variable = convert_datetime_date_to_saved_string(date_variable)
            break
        except:
            print("Please input the date in the correct format.")
            continue
    return date_variable

# assign tasks to users that already exist
def add_task(usernames):
    '''adds tasks for exising users and appends task to task.txt'''
    assigned_user = input("Enter the assigned user: ")
    task_title = input("Enter task title: ")
    task_desc = input("Enter task description: ")
    start_date = get_date_from_user_and_return_saved_date_string("Enter the start date (eg. 05 Feb 1994): ")
    due_date = get_date_from_user_and_return_saved_date_string("Enter the due date (eg. 05 Feb 1994): ")
    completed = "No\n"

    # print error message if username does not exist
    if assigned_user not in usernames:
        print("-----------------------------------")
        print("This user does not exist!")
        print("-----------------------------------")

    # add new task to the tasks.txt file
    else:
        with open("tasks.txt", "a+") as file:
            file.write(f"{assigned_user}, {task_title}, {task_desc}, {start_date}, {due_date}, {completed}")

# view all tasks in tasks.txt file
def view_all():
    '''prints all tasks from tasks.txt in readable format'''
    with open("tasks.txt", "r") as file:
        for lines in file:
            try:
                tasks = lines.strip()
                tasks = tasks.split(",")    # split string into a list at comma to get indexes
                username = tasks[0]         # assign variable names to indexes
                title = tasks[1]
                description = tasks[2]
                start_date = tasks[3]
                assigned_date = tasks[4]
                completed = tasks[5]

                # print information in readable format for user
                print("-----------------------------------")
                print(f"Username: {username}")
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Start date: {start_date}")
                print(f"Due date: {assigned_date}")
                print(f"Completed: {completed}")
                print("-----------------------------------")

            # catch exception error if index called is out of bounds
            except IndexError:
                continue

# view current users tasks
def view_mine(user_name):
    '''prints tasks from task.txt for current user'''
    # read tasks.txt file and split strings into list at the comma
    with open("tasks.txt", "r") as file_handle:
        task_list = [i.split(",") for i in file_handle.readlines()]

        task_id = 0
        task_id_index_link_dict = {}            # create dictionary
        has_tasks = False
        for index, task in enumerate(task_list):
            if task[0] == user_name:
                task_id += 1                    # if user has previous task, add one to task_id
                task_id_index_link_dict[task_id] = index
                has_tasks = True

                # print out numbered tasks for the user
                print("-----------------------------------")
                print(f"Task {task_id}")
                username = task[0]
                title = task[1]
                description = task[2]
                start_date = task[3]
                assigned_date = task[4]
                completed = task[5]
                print(f"Username: {username}, \n Title: {title}, \n Description: {description}, \n Start date: "
                      f"{start_date}, \n Due date: {assigned_date}, \n Completed: {completed}")
                print("-----------------------------------")

    # allow user to edit their tasks
    if has_tasks:
        while True:
            try:
                task_id_to_edit = int(input("Please type the number of the task to edit (-1 to exit): "))

                if task_id_to_edit == -1:
                    break

                task_to_edit = task_list[task_id_index_link_dict[task_id_to_edit]]

                edit_or_complete_task = input("Edit or complete task: ").lower()

                if edit_or_complete_task == "edit":

                    print("""
                    What would you like to edit?
                    u   - username
                    t   - title
                    d   - description
                    sd  - start date
                    dd  - due date
                    c   - completed
                    """)
                    parameter_to_edit = input(": ")
                    if parameter_to_edit == "u":
                        task_to_edit_input = input("New username: ")
                        if task_to_edit_input not in usernames:
                            print("-----------------------------------")
                            print("This user does not exist!")
                            print("-----------------------------------")

                        else:
                            task_to_edit[0] = task_to_edit_input

                    elif parameter_to_edit == "t":
                        task_to_edit[1] = input("New title: ")

                    elif parameter_to_edit == "d":
                        task_to_edit[2] = input("New description: ")

                    elif parameter_to_edit == "sd":
                        task_to_edit[3] = get_date_from_user_and_return_saved_date_string("Enter the start date (eg. 05 Feb 1994): ")

                    elif parameter_to_edit == "dd":
                        task_to_edit[4] = get_date_from_user_and_return_saved_date_string("Enter the due date (eg. 05 Feb 1994): ")

                    elif parameter_to_edit == "c":
                        task_completed = input("Task completed? y/n: ")

                        if task_completed.lower() == "y":
                            task_to_edit[5] = "Yes\n"
                        else:
                            task_to_edit[5] = "No\n"

                    else:
                        print("Your selection was not valid.")

                    task_list[task_id_index_link_dict[task_id_to_edit]] = task_to_edit

                    task_list_string_to_write = [",".join(i) for i in task_list]

                    with open("tasks.txt", "w") as file_handle:
                        file_handle.writelines(task_list_string_to_write)
                        file_handle.write("\n")

                elif edit_or_complete_task == "complete":
                    task_completed = input("Task completed? y/n: ").lower()

                    if task_completed == "y":
                        task_to_edit[5] = "Yes\n"
                    elif task_completed == "n":
                        task_to_edit[5] = "No\n"
                    else:
                        print("Choice not valid. Input should be y or n.")

                    task_list[task_id_index_link_dict[task_id_to_edit]] = task_to_edit

                    task_list = [",".join(i) for i in task_list]

                    with open("tasks.txt", "w") as file_handle:
                        file_handle.writelines(task_list)
                        file_handle.write("\n")

            # catch ValueError if inappropriate value is given
            except ValueError as exception_code:
                print(f"Error {exception_code}")
                continue

    else:
        print("-----------------------------------")
        print("You have no tasks.")
        print("-----------------------------------")

### CONVERT STRINGS TO LISTS ###

def convert_string_to_datetime_date(input_string):
    '''converts string to datetime date'''
    day, month_name, year = input_string.strip().split(" ")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = months.index(month_name)+1

    return date(int(year), int(month), int(day))

# convert date format to given format in tasks.txt
def convert_datetime_date_to_saved_string(datetime_date):
    '''takes datetime object and converts to string with format dd mmm yyyy'''
    return datetime_date.strftime("%d %b %Y")

# convert task strings into a list of tasks by splitting on comma and appending to end of list
def convert_task_strings_to_task_list(task_list_strings):
    '''converts task string and stores as list'''
    task_list = []
    for task_string in task_list_strings:
        task_string = task_string.split(",")
        try:
            task_string[3] = convert_string_to_datetime_date(task_string[3])
            task_string[4] = convert_string_to_datetime_date(task_string[4])
        except IndexError:
            continue
        task_list.append(task_string)
    return task_list

# convert user strings into a list of users by splitting on comma and appending to end of list
def convert_user_strings_to_user_list(user_list_strings):
    '''converts user string and stores as list'''
    user_list = []
    for user_string in user_list_strings:
        user_string = user_string.split(",")
        user_list.append(user_string)
    return user_list

### RETURN DATA FROM TASK_LIST ###

# to view how many users there are
def number_of_users():
    '''return number of users in user.txt'''
    with open("user.txt", "r") as file:
        num_users = len(file.readlines())  # amount of lines in file equals amount of users
    return num_users

# to view how many tasks there are
def number_of_tasks():
    '''returns number of tasks in tasks.txt'''
    with open("tasks.txt", "r") as file:
        num_tasks = len(file.readlines())  # amount of lines in file equals amount of tasks
    return num_tasks

# to view the number of all tasks that have been completed in task_list
def number_of_completed_tasks(task_list):
    '''returns number of tasks completed'''
    tasks_completed = 0
    for task in task_list:
        if task[5].strip() == "Yes":        # strip to remove any leading/trailing spaces
            tasks_completed += 1
    return tasks_completed

# to view the number of all tasks that have not been completed in task_list
def number_of_tasks_not_completed(task_list):
    '''returns number of tasks not completes'''
    tasks_not_completed = 0
    for task in task_list:
        if task[5].strip() == "No":
            tasks_not_completed += 1
    return tasks_not_completed

# to view the number of all tasks that are overdue in task_list
def number_of_tasks_overdue(task_list):
    '''returns number of tasks overdue'''
    tasks_overdue = 0
    for task in task_list:
        if task[4] < date.today() and task[5].strip() == "No":
            tasks_overdue += 1
    return tasks_overdue

# to view the percentage of all tasks that have not been completed in task_list
def percentage_of_incomplete_tasks(task_list):
    '''returns percentage of tasks not completed'''
    try:
        return (number_of_tasks_not_completed(task_list) / number_of_tasks()) * 100
    except ZeroDivisionError:
        return 0

# to view the percentage of all tasks that are overdue in task_list
def percentage_of_overdue_tasks(task_list):
    '''returns percentage of tasks overdue'''
    try:
        return (number_of_tasks_overdue(task_list) / number_of_tasks()) * 100
    except ZeroDivisionError:
        return 0

### RETURN USER SPECIFIC DATA FROM TASK_LIST ###

# return all tasks assigned to specific user
def tasks_assigned_to_user(task_list, username):
    '''returns number of tasks assigned to user'''
    number_of_tasks_assigned_to_user = 0
    for task in task_list:
        if task[0] == username:
            number_of_tasks_assigned_to_user += 1
    return number_of_tasks_assigned_to_user

# return percentage of tasks that have been assigned to specific user
def percentage_of_total_tasks_assigned_to_user(task_list, username):
    '''returns percentage of all tasks assigned to user'''
    try:
        return (tasks_assigned_to_user(task_list, username) / number_of_tasks()) * 100
    except ZeroDivisionError:
        return 0

# view the number of tasks assigned to user that are completed
def assigned_tasks_completed(task_list, username):
    '''returns number of tasks assigned to specific user that is completed'''
    user_tasks_completed = 0
    for task in task_list:
        if task[0] == username and task[5].strip() == "Yes":
            user_tasks_completed += 1
    return user_tasks_completed

# view the percentage of tasks assigned to user that are completed
def percentage_of_assigned_tasks_completed(task_list, username):
    '''returns percentage of tasks assigned to specific user that is completed'''
    try:
        return (assigned_tasks_completed(task_list, username) / tasks_assigned_to_user(task_list, username)) * 100
    except ZeroDivisionError:
        return 100

# view the number of tasks assigned to user that are not completed
def assigned_tasks_not_completed(task_list, username):
    '''returns number of tasks assigned to specific user that are not completed'''
    user_tasks_not_completed = 0
    for task in task_list:
        if task[0] == username and task[5].strip() == "No":
            user_tasks_not_completed += 1
    return user_tasks_not_completed

# view the percentage of tasks assigned to user that are not completed
def percentage_of_assigned_tasks_not_completed(task_list, username):
    '''returns percentage of tasks assigned to specific user that are not completed'''
    try:
        return (assigned_tasks_not_completed(task_list, username) / tasks_assigned_to_user(task_list, username)) * 100
    except ZeroDivisionError:
        return 0

# view the number of tasks assigned to user that are overdue
def assigned_tasks_overdue(task_list, username):
    '''returns number of tasks overdue for specific user'''
    user_tasks_overdue = 0
    for task in task_list:
        if task[0] == username and task[4] < date.today() and task[5].strip() == "No":
            user_tasks_overdue += 1
    return user_tasks_overdue

# view the percentage of tasks assigned to user that are overdue
def percentage_of_assigned_tasks_overdue(task_list, username):
    '''returns percentage of tasks overdue for specific user'''
    try:
        return (assigned_tasks_overdue(task_list, username) / tasks_assigned_to_user(task_list, username)) * 100
    except ZeroDivisionError:
        return 0

### MAIN FUNCTIONS CONTINUED ###

# display stats of number of users and tasks
def display_stats():
    '''prints number of tasks and number of users'''
    if user_name != 'admin':
        print("-----------------------------------")
        print("Displaying stats requires admin privileges.")
        print("-----------------------------------")
        return

    else:
        num_users = number_of_users()
        num_tasks = number_of_tasks()
        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")
        return

#function to generate reports
def generate_reports():
    '''calulates statistics and stores in task_overview.txt file'''
    if user_name != 'admin':
        print("-----------------------------------")
        print("Generating reports requires admin privileges.")
        print("-----------------------------------")
        return

    else:
        print("Reports generated...")
        with open("tasks.txt", "r") as file_handle:
            task_list = convert_task_strings_to_task_list(file_handle.readlines())
        with open("task_overview.txt", "w+") as task_overview_file_handle:
            task_overview_file_handle.write(f"Number of tasks: {number_of_tasks()}\n")
            task_overview_file_handle.write(f"Number of completed tasks: {number_of_completed_tasks(task_list)}\n")
            task_overview_file_handle.write(f"Number of incomplete tasks: {number_of_tasks_not_completed(task_list)}\n")
            task_overview_file_handle.write(f"Number of overdue tasks: {number_of_tasks_overdue(task_list)}\n")
            task_overview_file_handle.write(f"Percentage of incomplete tasks: {percentage_of_incomplete_tasks(task_list)}%\n")
            task_overview_file_handle.write(f"Percentage of overdue tasks: {percentage_of_overdue_tasks(task_list)}%\n")

        with open("user.txt", "r") as file_handle:
            user_list = convert_user_strings_to_user_list(file_handle.readlines())
        with open("user_overview.txt", "w+") as user_overview_file_handle:
            user_overview_file_handle.write(f"Number of users: {number_of_users()}\n")
            user_overview_file_handle.write(f"Number of tasks: {number_of_tasks()}\n")
            for username, _ in user_list:
                user_overview_file_handle.write(f"{'-' * 50}\n")
                user_overview_file_handle.write(f"Statistics for user [{username}]: \n")
                user_overview_file_handle.write(f"Tasks assigned: {tasks_assigned_to_user(task_list, username)}\n")
                user_overview_file_handle.write(f"Percentage of tasks assigned to user: "
                                                f"{percentage_of_total_tasks_assigned_to_user(task_list, username)}%\n")
                user_overview_file_handle.write(f"Percentage of assigned tasks completed: "
                                                f"{percentage_of_assigned_tasks_completed(task_list, username)}%\n")
                user_overview_file_handle.write(f"Percentage of assigned tasks not complete: "
                                                f"{percentage_of_assigned_tasks_not_completed(task_list, username)}%\n")
                user_overview_file_handle.write(f"Percentage of assigned tasks overdue: "
                                                f"{percentage_of_assigned_tasks_overdue(task_list, username)}%\n")

def get_users_from_file():
    '''reads users.txt file and returns all usernames and passwords'''
    # create empty lists for usernames and passwords
    usernames = []
    passwords = []

    #open user.txt file to read usernames and passwords, split to list for indexes
    with open("user.txt", "r") as file:
        for lines in file:
            temp = lines.strip()
            temp = temp.split(", ")

            usernames.append(temp[0])
            passwords.append(temp[1])

    return usernames, passwords


### USER INPUT ###

if __name__ == "__main__":
    usernames, passwords = get_users_from_file()

    # ask user to enter a username and password if not already logged on
    # only allow for new usernames to be available to new users
    logged_in = False
    while not logged_in:
        user_name = input("Please enter your username: ")
        pass_word = input("Please enter your password: ")

        if user_name not in usernames:
            print("Incorrect username, please try again")
            continue

        elif pass_word not in passwords:
            print("Incorrect password, please try again")
            continue

        else:
            print(f"Welcome, {user_name}, make a selection below...")
            logged_in = True

    # display a list of possible options and allow user to select one
    while logged_in:
        usernames, _ = get_users_from_file()

        if user_name == "admin":
            print("""
        r - register new user
        a - add new task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit program
        """)

        else:
            print("""
        r - register new user
        a - add new task
        va - view all tasks
        vm - view my tasks
        ds - display statistics
        e - exit program
        """)

    #depending on choice, launch desired function
        user_choice = input(": ")

        if user_choice == "r":      #Create a new user
            reg_user(usernames)

        elif user_choice == "a":    #Add new tasks
            add_task(usernames)

        elif user_choice == "va":   #View all tasks
            view_all()

        elif user_choice == "vm":   #View tasks assigned to current user
            view_mine(user_name)

        elif user_choice == "gr":   #If admin, generate report
            generate_reports()

        elif user_choice == 'ds':   #If admin, display statistics
            display_stats()

        elif user_choice == 'e':    #Exit program
            print(f"Goodbye {user_name}!")
            exit()

        else:                       #Print message to try again if input not valid
            print("This is not possible. Please Try again")