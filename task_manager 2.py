# import libraries
from datetime import datetime

# variables that make the outputs different colours, bold or underlined
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
BOLD = "\033[1m"
UNDERLINE = '\033[4m'
END = "\033[0m"

# dictionary that will store usernames and passwords
user_dict = {}
# create variable to store the username input by the user
username_input = ""


# define a function that registers a new user
def reg_user():
    # print a message to introduce the user's choice in cyan and bold
    print(f"\n{CYAN}{BOLD}——————————————— •REGISTER A USER• ———————————————{END}")

    # ask admin to input a new username for the user they want to register
    new_user = input("Please enter the username for the new user: \t")

    # while the new username already exists
    #   print a message in red to signal the user already exists and input a different username
    #   ask admin to input a new username for the user they want to register
    while new_user in user_dict:
        print(f"{RED}This User Already Exists. Please Register A Different Username.{END}")
        new_user = input("Please enter the username for the new user: \t")

    # if the username the admin would like to assign the new user is not in the user dictionary
    #   ask the admin to input the new password for the new user
    #   ask the admin to confirm the new password
    if new_user not in user_dict:
        new_psw = input("Please enter the password for the new user: \t")
        confirm_psw = input("Please confirm the password for the new user: \t")
        # while the new password and the password confirmation do not match
        #   print a message in red to say they do not match and prompting them to try again
        #   ask for the new password and the password confirmation again
        while new_psw != confirm_psw:
            print(f"{RED}Your Password Confirmation Does Not Match. Please Try Again.{END}")
            new_psw = input("Please enter the password for the new user: \t")
            confirm_psw = input("Please confirm the password for the new user: \t")
        # if the new password and the password confirmation match
        #   print a statement in green saying the operation has been successful
        #   write the new username and password to the file
        if new_psw == confirm_psw:
            print(f"\n{GREEN}Operation Successful. Thank You For Registering A New User.{END}")
            f.write(f"\n{new_user}, {new_psw}")


# define a function for the user to add a task
def add_task():
    # print a message in cyan and bold to introduce the function
    print(f"\n{CYAN}{BOLD}——————————————— •ADD TASK• ———————————————{END}")
    # print a statement asking the user to enter the following data
    print("Please enter the following data:")

    # ask the user to input the username of the person the task is assigned to
    user_assigned = input("The username of the person assigned to the task: \t")
    # while the user is not in the user dictionary
    #   print a statement in red to say the user is not registered and prompting them to try again
    #   ask the user to enter the username of the person assigned to the task again
    while user_assigned not in user_dict:
        print(f"{RED}This User Is Not Registered. Please Try Again.{END}")
        user_assigned = input("The username of the person assigned to the task: \t")
    # if the username of the user assigned the task is in the user dictionary
    #   ask the user for the title of the task
    #   ask the user for a description of the task
    #   ask the user to enter the deadline of the task in the correct format
    #   if the date is not in the correct format then print a message in red to say it is incorrect and to try again
    #   get the current date
    #   create a variable to signal whether the task is complete and give it the value "No"
    if user_assigned in user_dict:
        task_title = input("The title of the task: \t\t\t\t\t\t\t\t")
        task_description = input("A description for the task: \t\t\t\t\t\t")
        # FOR REFERENCE:
        # the supplementary lecture on this capstone helped me implement the error handling with regards to
        # the user inputting the correct date format
        # I tried to do this using if statements and was getting error messages
        # it was suggested in the supplementary lecture to implement a try/except statement which
        # I have implemented into the program
        while True:
            try:
                task_deadline = input("The date the task is due (DD Mon YYYY): \t\t\t")
                datetime.strptime(task_deadline, "%d %b %Y")
                break
            except:
                print(f"{RED}Invalid date. Please ensure you have used the correct format.{END}")
        current_date = datetime.today().strftime("%d %b %Y")
        task_complete = "No"

        # print a statement in green to say the operation has been successful
        # write the information gathered above to the file
        print(f"\n{GREEN}Operation Successful. Thank You For Adding A New Task{END}")
        f.write(f"\n{user_assigned}, {task_title}, {task_description}, {task_deadline}, {current_date}, {task_complete}")


# define a function to view all tasks
def view_all():
    # print a statement in cyan and bold to introduce this function/user choice
    print(f"{CYAN}{BOLD}——————————————— •ALL TASKS• ———————————————{END}\n")
    # for each line in the given file from the main code section
    #   split the line using the comma as a delimiter
    #   print the following from the file in a user-friendly format
    #   the task title
    #   the user assigned to the task
    #   the date the task was assigned i.e. the current date
    #   the deadline date for the task
    #   whether the task is complete or not
    #   the task description
    for line in f:
        line = line.split(", ")
        print(f"Task:\t\t\t\t\t\t{line[1]}")
        print(f"Assigned to:\t\t\t\t{line[0]}")
        print(f"Date assigned:\t\t\t\t{line[4]}")
        print(f"Due date:\t\t\t\t\t{line[3]}")
        print(f"Task Complete?:\t\t\t\t{line[5]}")
        print(f"Description of the task:\n{line[2]}")
        # print a long line to separate the tasks from each other
        print("\n—————————————————————————————————————————————————————————\n")


# define a function for the user to view their specific tasks and allows them to edit them
def view_mine():
    # print a statement in cyan and bold to introduce this option
    print(f"{CYAN}{BOLD}——————————————— •MY TASKS• ———————————————{END}\n")
    # create a dictionary to store all the tasks
    tasks_dict = {}
    # create a dictionary to store the user's tasks
    user_tasks = {}

    # create a variable assigning a number to the tasks and initialise to 0
    task_num = 0
    # create a variable assigning a number to the user's tasks and initialise to 1
    user_task_num = 1

    # for each line of the file
    #   strip the line of the new line escape character and split it using the comma as a delimiter
    #   increment the task number by 1
    #   store the task number and the line in the tasks dictionary
    for line in f:
        line = line.strip("\n").split(", ")
        task_num += 1
        tasks_dict[task_num] = line
        # if the user's username is equal to the username of the username in the tasks dictionary
        #   print a message to display the following data from the tasks file in an easy-to-read manner:
        #   the task
        #   the user assigned to the task
        #   the date the task was assigned i.e. the current date
        #   the deadline date for the task
        #   whether the task is complete or not
        #   the task description
        if username_input == line[0]:
            print(f"——————————————— •Task {user_task_num}• ———————————————\n")
            print(f"Task:\t\t\t\t\t\t{line[1]}")
            print(f"Assigned to:\t\t\t\t{line[0]}")
            print(f"Date assigned:\t\t\t\t{line[4]}")
            print(f"Due date:\t\t\t\t\t{line[3]}")
            print(f"Task Complete?:\t\t\t\t{line[5]}")
            print(f"Description of the task:\n{line[2]}")
            print("\n—————————————————————————————————————————\n")
            # store the task for that user in the user tasks dictionary with the number of the user's task as the key and
            # the overall number of the task as a value
            user_tasks[user_task_num] = task_num
            # increment the task number in the user's tasks by 1
            user_task_num += 1
    # create a variable to store the user's edit choice and initialise to 0
    user_edit = 0
    # while the user's edit choice does not equal -1
    #   present a choice to the user as to which of their tasks they would like to edit
    #   or pick -1 to return to the main menu
    while user_edit != -1:
        user_edit = int(input(f'''\n{BOLD}If You Would Like To Edit One Of Your Tasks{END}
Please enter the number of the task you'd like to edit
{UNDERLINE}or{END} enter -1 to return to you user menu"
: '''))

        # if the user's edit choice is bigger than 0 and smaller than the largest task number of the user's tasks and
        #   if the user's username is equal to the username found in the tasks dictionary
        #       print a message to introduce the options of the editing menu including
        #       tc to mark the task as complete
        #       un to edit the username assigned to the task
        #       dd to edit the due date of the task
        #       convert to lowercase to ensure the way the user capitalises their input does not affect the output
        if user_edit > 0 and user_edit < user_task_num:
            if username_input == tasks_dict[user_tasks[user_edit]][0]:
                print(f"{PURPLE}——————————————— •Editing Menu• ———————————————{END}\n")
                edit_menu = input('''Please select one of the following editing options:
• tc –\tMark the task as complete
• un –\tEdit the username assigned to the task
• dd –\tEdit the due date of the task
: ''').lower()
                # if the user chooses "tc"
                #   change the task completion from "No" to "Yes"
                #   join this with the rest of the tasks in the tasks dictionary and store as a list
                #   open the tasks.txt file to write to
                #   convert the new list with all the tasks in it to a string separating each item with a new line and
                #   write to the file
                if edit_menu == "tc":
                    tasks_dict[user_tasks[user_edit]][-1] = "Yes"
                    all_tasks = [", ".join(task) for task in tasks_dict.values()]
                    with open("tasks.txt", "w") as tasks_file:
                        tasks_file.write("\n".join(all_tasks))

                # if the user choose "un"
                #   ask the username of the person they would like to assign the task to
                elif edit_menu == "un":
                    user_change = input("Which user would you like to assign this task to: ")

                    # while the username they would like to change the assignment of the task to is not
                    # in the user dictionary
                    #   print a statement in red signalling that the user does not exist and to try again
                    #   ask the username of the person they would like to assign the task to again
                    while user_change not in user_dict:
                        print(f"{RED}This User Does Not Exist. Please Try Again.{END}")
                        user_change = input("Which user would you like to assign this task to: ")
                    tasks_dict[user_tasks[user_edit]][0] = user_change
                    all_tasks = [", ".join(task) for task in tasks_dict.values()]
                    with open("tasks.txt", "w") as tasks_file:
                        tasks_file.write("\n".join(all_tasks))

                # if the user chooses "dd" to edit the due date of the task
                #   ask the user to enter the new due date in the correct format and then add it to the file
                #   if the user does not enter the date in the correct format then display a message in red and
                #   prompt them to try again
                elif edit_menu == "dd":
                    while True:
                        try:
                            new_deadline = input("Please enter the new due date for the task (DD Mon YYYY): ")
                            datetime.strptime(new_deadline, "%d %b %Y")
                            tasks_dict[user_tasks[user_edit]][3] = new_deadline
                            all_tasks = [", ".join(task) for task in tasks_dict.values()]
                            with open("tasks.txt", "w") as tasks_file:
                                tasks_file.write("\n".join(all_tasks))
                                break
                        except:
                            print(f"{RED}Invalid Date Format. Please Try Again Using The Correct Date Format.{END}")

        # if the user enters -1 when entering the number of the task they would like to edit then break the loop to
        # return to the main menu
        elif user_edit == -1:
            break

        # if the user types anything else other than the options provided then
        # print a message in red telling them this is invalid and prompt them to try again
        else:
            print(f"{RED}Invalid Option. Please Type A Valid Option From the Task Edit Menu. {END}")


# define a function that generates a tasks report
def tasks_report():
    # open the tasks file to read
    # convert to a list
    # close the file
    tasks_file = open("tasks.txt", "r")
    tasks_lines = tasks_file.readlines()
    tasks_file.close()

    # find the total number of tasks and store
    total_tasks = len(tasks_lines)

    # create variable and initialise to 0 that will be used to find the following
    # the total number of complete tasks
    # the total number of incomplete tasks
    # the total number of tasks that are both incomplete and overdue
    total_complete = 0
    total_incomplete = 0
    total_overdue = 0

    # for each line of the list storing the tasks
    #   strip the new line escape character and split using the comma as a delimiter
    #   find whether the task has been completed by checking the index position in the tasks list
    #   if it says yes then
    #       increment the total completed tasks by 1
    #   if it does not
    #       then increment the total incomplete tasks by 1
    #       find the due date of the task
    #       convert the due date string to a date object
    #       get the current date using datetime
    #       if the due date object is smaller than the current date
    #           increment the total overdue by 1
    for line in tasks_lines:
        tasks_list = line.strip("\n").split(", ")
        completed_tasks = tasks_list[5]
        if completed_tasks.lower() == "yes":
            total_complete += 1
        else:
            total_incomplete += 1
            due_date = tasks_list[-3]
            date_obj = datetime.strptime(due_date, "%d %b %Y")
            curr_date = datetime.today()
            if date_obj < curr_date:
                total_overdue += 1

    # calculate the percentage of tasks that are incomplete
    percentage_incomplete = round(total_incomplete / total_tasks * 100, 2)
    # calculate the percentage of tasks that are incomplete and overdue
    percentage_overdue = round(total_overdue / total_tasks * 100, 2)

    # open a new tasks overview file to write into
    # write the following information to it in a readable format:
    #   the total number of tasks generated and task by the program
    #   the total number of completed tasks
    #   the total number of incomplete tasks
    #   the total number of incomplete and overdue tasks
    #   the percentage of incomplete tasks
    #   the percentage of incomplete and overdue tasks
    # then close the file
    f = open("tasks_overview.txt", "w")
    f.write(f'''The total number of tasks in the system: \t\t\t{total_tasks}
The total number of completed tasks: \t\t\t\t{total_complete}
The total number of incomplete tasks: \t\t\t\t{total_incomplete}
The total number of incomplete and overdue tasks: \t{total_overdue}
The percentage of incomplete tasks: \t\t\t\t{percentage_incomplete}%
The percentage of overdue tasks: \t\t\t\t\t{percentage_overdue}%''')
    f.close()


# define a function that generates a user report
def user_report():
    # open both the user and tasks files, convert them to lists and close the files
    users_file = open("user.txt", "r")
    user_lines = users_file.readlines()
    users_file.close()
    tasks_file = open("tasks.txt", "r")
    tasks_lines = tasks_file.readlines()
    tasks_file.close()

    # open a new user overview file to write into
    f = open("user_overview.txt", "w")

    # find the total number of users and tasks then write these to the file
    total_users = len(user_lines)
    total_tasks = len(tasks_lines)
    f.write(f'''The total number of users registered with the Task Manager: \t\t\t\t{total_users}
The total number of tasks generated and tracked using the Task Manager: \t{total_tasks}\n''')

    # for each user in the list storing the users
    #   strip the line of the new line characters and split by the commas
    #   create variables that will store the following and initialise to 0:
    #   the total number of tasks for each user
    #   the total number of completed tasks for each user
    #   the total number of incomplete tasks for each user
    #   the total number of incomplete and overdue tasks for each user
    for user in user_lines:
        user = user.strip("\n").split(", ")
        user_tasks_total = 0
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0

        # for each task in the list storing the tasks
        #   strip the line of the new line characters and split by the commas
        for task in tasks_lines:
            task = task.strip("\n").split(", ")

        # if the username in the user list and the tasks list match
        #   increment that user's total tasks by 1
        #   find the index that stores whether the task is completed in the tasks list
        #   if it says yes then
        #       increment the user's total number of tasks completed by 1
        #   if not then
        #       increment the user's incomplete tasks by 1
        #       find the due date of the task
        #       convert the due date string to a date object
        #       get the current date using datetime
        #       if the due date object is smaller than the current date
        #           increment the total overdue by 1
            if user[0] == task[0]:
                user_tasks_total += 1
                complete_tasks = task[5]
                if complete_tasks.lower() == "yes":
                    user_complete += 1
                else:
                    user_incomplete += 1
                    user_deadline = task[-3]
                    deadline_obj = datetime.strptime(user_deadline, "%d %b %Y")
                    today_date = datetime.today()
                    if deadline_obj < today_date:
                        user_overdue += 1

        # if the total number of tasks that user has does not equal 0
        #   calculate the percentage of tasks assigned to that user
        #   calculate the percentage of tasks that user has completed
        #   calculate the percentage of tasks the user has not completed
        #   calculate the percentage of tasks the user has not completed and are overdue
        if user_tasks_total != 0:
            user_percentage = round(user_tasks_total / total_tasks * 100, 2)
            complete_percent = round(user_complete / user_tasks_total * 100, 2)
            incomplete_percent = round(user_incomplete / user_tasks_total * 100, 2)
            overdue_percent = round(user_overdue / user_tasks_total * 100, 2)

        # if the total number of tasks that user has does equal 0
        #   then all the percentages from above also equal zero
        else:
            user_percentage = 0
            complete_percent = 0
            incomplete_percent = 0
            overdue_percent = 0

        # write the following information to the user overview file in a readable format
        #   the total number of tasks assigned to the user
        #   the percentage of tasks assigned to the user
        #   the percentage of tasks the user has completed
        #   the percentage of tasks that user has not completed
        #   the percentage of tasks that user has not completed and are overdue
        f.write(f'''\n\n{user[0].capitalize()}'s task statistics:
    The total number of tasks assigned to this user: \t\t\t\t\t\t\t\t{user_tasks_total}
    The percentage of the tasks that have been assigned to this user: \t\t\t\t{user_percentage}%
    The percentage of tasks assigned to this user that are completed: \t\t\t\t{complete_percent}%
    The percentage of tasks assigned to this user that are not completed: \t\t\t{incomplete_percent}%
    The percentage of tasks assigned to this user that are incomplete and overdue: \t{overdue_percent}%''')

# close the file
    f.close()


# define a function that will display the statistics in the tasks and user reports
def display_stats():
    # open both the tasks overview and user overview files to read into
    user_file = open("user_overview.txt", "r")
    tasks_file = open("tasks_overview.txt", "r")

    # store these files in their original formats
    user_lines = user_file.read()
    tasks_lines = tasks_file.read()

    # print headings in cyan and bold to introduce the tasks report and print the tasks overview file
    print(f"\n{CYAN}{BOLD}——————————————— •TASK REPORT• ———————————————{END}")
    print(f"{tasks_lines}\n")

    # print a heading in cyan and bold to introduce the user report and print the user overview file
    print(f"\n{CYAN}{BOLD}——————————————— •USER REPORT• ———————————————{END}")
    print(user_lines)

    # close both files
    user_file.close()
    tasks_file.close()


# introduce the user to the login system
print(f"{YELLOW}{BOLD}———————————————————— •Welcome To The Login• ———————————————————————{END}")

# open the user.txt file to read into
f = open("user.txt", "r")

# create a boolean that will be used to check the credentials of the user are correct
credential_check = False

# for each line of the user.txt file
#   strip the new line character and split using the comma as a separator
#   add the username and password to the user dictionary
#   with the username as the key and the password as the value
for line in f:
    username, password = line.strip("\n").split(", ")
    user_dict[username] = password

# while false
#   ask the user to input their username
#   ask the user to input their password
while not credential_check:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")

    # if the username is in the user dictionary
    #   if the password in equal to the password value for that username in the dictionary
    #       change the credentials boolean to True and
    #       print a statement in green saying the login was successful
    if username_input in user_dict:
        if password_input == user_dict[username_input]:
            credential_check = True
            print(f"\n{GREEN}Login Successful! Welcome {username_input.capitalize()}!{END}")
    # if the credential checker is false
    #   print a message in red saying their credentials are invalid and prompt them to try again
    if not credential_check:
        print(f"\n{RED}Invalid credentials. Please try again.{END}")

# close the user.txt file
f.close()

# create while loop to present a selection menu to the user and
# to carry out all the options in the menu
while True:
    # if the user's username is admin
    #   print a heading in purple and bold to introduce the admin selection menu
    if username_input == "admin":
        print(f"{PURPLE}{BOLD}—————————————— •ADMIN SELECTION MENU• —————————————————{END}")

        # present the menu to the admin so that they can type the following to do a specific action, including:
        # r for registering a user
        # a for adding a task
        # va to view all tasks
        # vm to view tasks assigned to them only
        # vs to view statistics i.e. the total number of tasks and users on the system
        # e to exit the menu
        # make sure to convert their input to lowercase so that the case the admin uses does not affect the output
        menu = input('''Please select one of the following options below:
• r - \tRegister a user
• a - \tAdd a task
• va - \tView all tasks
• vm - \tView my tasks
• gr - \tGenerate reports
• ds - \tDisplay statistics
• e - \tExit
: ''').lower()

    # if the user does not have the admin username
    #   print a heading in the same format at the previous heading to introduce the user selection menu
    else:
        print(f"{PURPLE}{BOLD}————————————————— •{username_input.upper()} SELECTION MENU• ———————————————————{END}")

        # present the menu to the user in the same manner and format as the admin selection menu, however
        # do not include the r or the vs options
        # make sure to convert their input to lowercase so that the case the user uses does not affect the output

        menu = input('''Please select one of the following options below:
• a - \tAdding a task
• va - \tView all tasks
• vm - \tView my tasks
• gr - \tGenerate reports
• e - \tExit
: ''').lower()

    # if the user has the username admin and
    # has chosen 'r' from the menu to register a new user
    #   open the user.txt file to append into
    #   call the function that registers the user
    #   close the user file
    if username_input == "admin" and menu == "r":
        f = open("user.txt", "a")
        reg_user()
        f.close()

    # if the user chooses 'a' to add a task
    #   open the tasks.txt file to append into
    #   call the function that adds a task to the file
    #   close the tasks file
    elif menu == "a":
        f = open("tasks.txt", "a")
        add_task()
        f.close()

    # if the user chooses 'va' to view all tasks
    #   open the tasks.txt file to read into
    #   call the function that allows the user to view all the tasks in the tasks file
    #   close the tasks file
    elif menu == "va":
        f = open("tasks.txt", "r")
        view_all()
        f.close()

    # if the user choose 'vm' to view the tasks assigned to them
    #   open the tasks file to read into as f
    #   call the view_mine function
    elif menu == "vm":
        with open("tasks.txt", "r") as f:
            view_mine()

    # if the user chooses 'gr' to generate reports
    #   call the function that generates the tasks report
    #   call the function that generates the user report
    #   print a message in green to say that the operation was successful
    elif menu == "gr":
        tasks_report()
        user_report()
        print(f"\n{GREEN}Operation Successful. Thank You For Generating New Reports.{END}")

    # if the username of the user is admin and they choose 'ds' to display statistics
    #   call the task report and the user report function to generate them
    #   call the function to display these reports to the user
    #   print a statement in green to signal the operation has been successful
    elif username_input == "admin" and menu == "ds":
        tasks_report()
        user_report()
        display_stats()
        print(f"\n{GREEN}Operation Successful. Thank You For Displaying Statistics.\n{END}")

    # if the user chooses 'e' to exit the program
    #   print a statement in yellow with thanking them for using the program
    #   make sure that there is a blank line above the statement
    #   exit the loop
    elif menu == 'e':
        print(f"\n{YELLOW}Thank You For Using The Task Manager. Have A Lovely Day!{END}")
        exit()

    # if the user has typed something other than the characters used to select a choice from the menu
    #   print a message in red stating that they have made an invalid selection and to try again
    #   make sure that there is a blank line above the statement
    else:
        print(f"\n{RED}Invalid Selection. Please Try Again.{END}")
        