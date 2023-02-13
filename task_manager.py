# import the date from datetime module
from datetime import date

# variables to differentiate outputs making them different colours and/or bold:
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
BOLD = "\033[1m"
END = "\033[0m"

# print a heading in yellow and bold to introduce the login system for the program
print(f"{YELLOW}{BOLD}———————————————————— •Welcome To The Login• ———————————————————————{END}")

# open the user.txt to file to read
f = open("user.txt", "r")
# read the lines of the file and convert to list
lines = f.readlines()

# create two empty lists
# one will store the usernames and the other will store the passwords in the file
username_list = []
password_list = []

# create two string variables to store the username and password the user will input
username_input = ""
password_input = ""

# for each line in the lines list
#   strip the new line character and split using the comma as a separator
#   append the username in index 0 to the username list
#   append the password in index 1 to the password list
for line in lines:
    username, password = line.strip("\n").split(", ")
    username_list.append(username)
    password_list.append(password)

# create a boolean variable that will be used in checking the credentials of the user
# set it to False
credential_correct = False

# while false
#   ask the user to input their username
#   ask the user to input their password
while not credential_correct:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")

    # if the username the user inputs is in the username list
    #   find the index position of that username in the list
    if username_input in username_list:
        pos = username_list.index(username_input)

        # if the password input is in the password list and has the same index position as the username input
        #   change the credential boolean created earlier to True
        #   print a statement in green to welcome the user with blank line above
        if password_input in password_list[pos]:
            credential_correct = True
            print(f"\n{GREEN}Login Successful! Welcome {username_input}!{END}")

    # failing all this, if the credential checker is false
    #   print a message saying their credentials are invalid and prompt them to try again
    #   print this statement in red with blank line above
    if not credential_correct:
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
• vs - \tView statistics
• e - \tExit
: ''').lower()

    # if the user does not have the admin username
    #   print a heading in the same format at the previous heading to introduce the user selection menu
    else:
        print(f"{PURPLE}{BOLD}————————————————— •USER SELECTION MENU• ———————————————————{END}")

        # present the menu to the user in the same manner and format as the admin selection menu, however
        # do not include the r or the vs options
        # make sure to convert their input to lowercase so that the case the user uses does not affect the output
        menu = input('''Please select one of the following options below:
• a - \tAdding a task
• va - \tView all tasks
• vm - \tView my tasks
• e - \tExit
: ''').lower()

    # if the user has the username admin and
    # has chosen 'r' from the menu to register a new user
    #   print a statement to introduce the user's selection in cyan and bold with
    #   a new line escape character at the beginning.
    if username_input == "admin" and menu == "r":
        print(f"\n{CYAN}{BOLD}——————————————— •REGISTER A USER• ———————————————{END}")

        # open the user.txt file to append data into it
        f = open("user.txt", "a")

        # ask admin to input a new username for the user they want to register
        new_user = input("Please enter the username for the new user: \t")
        if new_user in username_list:
            print(f"{RED}This user already exists{END}")
        else:
            # ask admin to input a new password for the new user
            new_psw = input("Please enter the password for the new user: \t")
            # ask admin confirm the password by writing it again
            confirm_psw = input("Please confirm the password for the new user: \t")

            # while the new password and password confirmation do not match
            #   print a message in red saying they do not match and prompting them to try again
            #   ask admin to input the new password and the password confirmation again
            while new_psw != confirm_psw:
                print(f"{RED}Your Password Confirmation Does Not Match.Please Try Again.{END}")
                new_psw = input("Please enter the password for the new user: \t")
                confirm_psw = input("Please confirm the password for the new user: \t")

            # if the new password and the password confirmation match
            #   print a message in green saying the registration has been successful and thank them
            #   write the new username and password to the user.txt file
            if new_psw == confirm_psw:
                print(f"\n{GREEN}Operation Successful. Thank You For Registering A New User.{END}")
                f.write(f"\n{new_user}, {new_psw}")

            # close the file
            f.close()

    # if the user selects 'a' to add a new task to the tasks.txt file
    #   print a heading to introduce the user's selection
    #   make sure it is formatted in the same way as the previous heading
    elif menu == "a":
        print(f"\n{CYAN}{BOLD}——————————————— •ADD TASK• ———————————————{END}")

        # open the tasks.txt file to append data to it
        f = open("tasks.txt", "a")

        # print a statement asking the admin to enter the following data
        print("Please enter the following data:")
        # ask the user to input the username of the person the task is assigned to
        user_assigned = input("The username of the person assigned to the task: \t")

        # while the user assigned to the task is not registered in the system
        #   print a statement in red stating the user is not registered and to try again
        #   ask the user to input the username of the person assigned to the task again
        while user_assigned not in username_list:
            print(f"{RED}This User Is Not Registered. Please Try Again.{END}")
            user_assigned = input("The username of the person assigned to the task: \t")

        # if the user assigned to the task is registered
        #   ask the user to input the title of  the task
        #   ask the user to input a description of the task
        #   ask the user the due date of the task in the same date format as in the tasks.txt file
        if user_assigned in username_list:
            task_title = input("The title of the task: \t\t\t\t\t\t\t\t")
            task_description = input("A description for the task: \t\t\t\t\t\t")
            task_deadline = input("The date the task is due (Day Mon Year): \t\t\t")

            # find the current date
            # for reference:
            # I did not know how to do this, so I found this article from Programiz which explained how to do this:
            # 'How to get current date and time in python?' Programiz. Available at:
            # https://www.programiz.com/python-programming/datetime/current-datetime (Accessed: January 5, 2023).
            # from this I learnt how to get the current date using the date class in the datetime module and
            # learnt how to format it using the strftime() method with help the following article
            # 'Python strftime()' Programiz. Available at:
            # https://www.programiz.com/python-programming/datetime/strftime (Accessed: January 6, 2023).
            # I implemented the appropriate format codes so that the date would be consistent those in the tasks file
            current_date = date.today().strftime("%d %b %Y")

            # create a variable to indicate whether the task is complete or not and assign it the value 'No'
            task_complete = "No"

            # print a message in green to say the new task has been added and thank the user for adding it
            # make sure there are blank lines above it
            print(f"\n{GREEN}Operation Successful. Thank You For Adding A New Task{END}")

            # write the new username and password to the tasks.txt file
            f.write(f"\n{user_assigned}, {task_title}, {task_description}, {task_deadline}, {current_date}, {task_complete}")

            # close the file
            f.close()

    # if the user chooses 'va' to view all existing tasks
    #   print a statement to introduce all the tasks
    #   make sure it is formatted in the same way as the previous heading
    elif menu == "va":
        print(f"{CYAN}{BOLD}——————————————— •ALL TASKS• ———————————————{END}\n")

        # open the tasks.txt file to read it
        f = open("tasks.txt", "r")

        # for each line in the tasks file
        #   convert the line to a list using the comma as the delimiter
        #   print statements displaying the following data found in the tasks file in an easy-to-read format:
        #   the task
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

        # close the file
        f.close()

    # if the user selects 'vm' to view the tasks specifically assigned to them
    #   print a statement to introduce the tasks assigned to the user
    #   ensuring it is in the same format as the previous selection headings
    elif menu == "vm":
        print(f"{CYAN}{BOLD}——————————————— •MY TASKS• ———————————————{END}\n")

        # open the tasks file to read
        f = open("tasks.txt", "r")

        # for each line in the file
        #   convert the line into a list
        for line in f:
            line = line.split(", ")

            # if the user's username is equal to the string in index position 0 of the line
            #   print a message to display the following data from the tasks file in an easy-to-read manner:
            #   the task
            #   the user assigned to the task
            #   the date the task was assigned i.e. the current date
            #   the deadline date for the task
            #   whether the task is complete or not
            #   the task description
            if username_input == line[0]:
                print(f"Task:\t\t\t\t\t\t{line[1]}")
                print(f"Assigned to:\t\t\t\t{line[0]}")
                print(f"Date assigned:\t\t\t\t{line[4]}")
                print(f"Due date:\t\t\t\t\t{line[3]}")
                print(f"Task Complete?:\t\t\t\t{line[5]}")
                print(f"Description of the task:\n{line[2]}")

                # print a long line to separate the tasks from each other with
                # a blank line above and below it
                print("\n—————————————————————————————————————————————————————————\n")

        # close the file
        f.close()

    # if the user's username is admin, and they have chosen 'vs' to view the statistics
    #   print a heading introducing the stats in the same format as previous headings
    elif username_input == "admin" and menu == "vs":
        print(f"{CYAN}{BOLD}——————————————— •STATISTICS• ———————————————{END}\n")

        # open the tasks.txt
        # read each line of the file and store as a list
        # print the total number of tasks by finding the length of the list
        # close the file
        # repeat these steps for the user.txt file
        tasks_file = open("tasks.txt", "r")
        tasks_lines = tasks_file.readlines()
        print(f"Total number of tasks: {len(tasks_lines)}")
        tasks_file.close()
        user_file = open("user.txt", "r")
        user_lines = user_file.readlines()
        print(f"Total number of users: {len(user_lines)}")
        user_file.close()

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
