# Student class → blueprint for creating student objects
class Student:

     # constructor → runs automatically when object is created
    def __init__(self, name,gender,Date_of_birth,phone_number,
                 password,bachelor,CAMPUS,study_time,academic_year):
        self.name = name
        self.gender = gender
        self.Date_of_birth = Date_of_birth
        self.phone_number = phone_number
        self.password = password
        self.bachelor = bachelor
        self.CAMPUS = CAMPUS
        self.study_time = study_time
        self.academic_year = academic_year


    def show_info(self):

        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Date of birth:",self.Date_of_birth)
        print("bachelor:",self.bachelor)
        print("CAMPUS:",self.CAMPUS)
        print("Time:",self.study_time)
        print("Academic year:",self.academic_year)

# School class → manages all students       
class School:

     # constructor → creates empty student list
    def __init__(self):
        self.Student = [] # list to store student objects

    #show school info
        self.school_name = "National university of management"
        self.location = "Phnom penh, Cambodia"
        self.web = "numuniversity.com"
        self.founded = 1983
        self.programs = "Bachelor","Master","phD"
        self.campus = "WatPhnom Campus", "Vealsbov Campus"
        self.contact = "+855 95 504 179"

    def school_info(self):
        print("======School Information======")
        print("Name:",self.school_name)
        print("Location:",self.location)
        print("Website:",self.web)
        print("Founded:",self.founded)
        print(f"Programs: {self.programs}")
        print(f"Campus: {self.campus}")
        print("Contact",self.contact)
        print("============")

    # register function → create new student
    def register(self):

        print("======Register======")

        # take user input
        name = input("Enter your name: ")
        gender = input("Enter gender: ")
        # store date as tuple (day, month, year)
        day = int(input("Enter Day of birth: "))
        month = input("Enter month of birth: ")
        year = int(input("Enter year of birth: "))
        Date_of_birth = f"{day} {month} {year}"
        bachelor = input("Enter bachelor: ")
        phone_number = int(input("Enter your phone number: "))
        password = int(input("Create Password: "))

        #CAMPUS choice
        print("Choose CAMPUS")
        print("1:WatPhnom Campus")
        print("2:Vealsbov Campus")

        campus_choice = input("Enter choice: ")

        if campus_choice == "1":
            CAMPUS = "WatPhnom Campus"
        elif campus_choice == "2":
            CAMPUS = "Vealsbov Campus"
        else:
            CAMPUS = "unknown"

        # Study time choice
        print("Choose Time")
        print("1:7:00-10:00")
        print("2:10:30-13:30")
        print("3:14:00-17:00")
        print("4:17:30-20:30")

        time_choice = input("Enter choice: ")

        if time_choice == "1":
            study_time = "7:00-10:00"
        elif time_choice == "2":
            study_time = "10:30-13:30"
        elif time_choice == "3":
            study_time = "14:00-17:00"
        elif time_choice == "4":
            study_time = "17:30-20:30"
        else:
            study_time = "unknown"

        academic_year = input("Enter Academic year: ")

        # create new student object
        new_student = Student(
            name,gender,Date_of_birth,
            phone_number,password,bachelor,
            CAMPUS,study_time,academic_year
            )
        print("\n======Register successfully!======")

        # add student object into list
        self.Student.append(new_student)

        # show student info
        new_student.show_info()

    # login function → check if phone_number + password match
    def login(self):

        print("\n======Login======")

        # ask login info
        phone = int(input("Enter phone number:"))
        pw = int(input("Enter your password:"))

        # flag variable to check if account exists
        found = False

        # loop through all students
        for student in self.Student:
            if student.phone_number == phone:
                if student.password == pw:
                    print("\nLogin successfully")
                    student.show_info()
                    found = True
                    break
                else:
                    print("\nLogin fail")
                    return
            
        if not found:
            print("Account not found!\n")

    # change password function
    def change_password(self):

        print("\n======Change Password======")

        phone = int(input("Enter your phone number:"))
        old_pw = int(input("Enter your old password:"))

        # loop through students
        for student in self.Student:

            # verify identity first
            if student.phone_number == phone and student.password == old_pw:
                new_password = int(input("Create new password:"))
                confirm_new_password = int(input("Confirm Password:"))
            
                if new_password == confirm_new_password:
                    student.password = new_password
                    print("Password changed successfully\n")
                else:
                    print("Try again\n")

                return # stop loop after changing password
        
        print("Account not found or wrong password!\n")

    # main menu function → program controller
    def school_menu(self):

        # infinite loop until exit
        while True:
            print("=========National university of management==========")
            print("1:Register")
            print("2:Login My account")
            print("3:Change Password")
            print("4:School Information")
            print("5:Exit")
            print("=========Choose option==========")
            choice = input("Enter your choice: ")

            # match-case → like switch statement
            match choice:
                case "1":
                    self.register() # call register function
                case "2":
                    self.login()  # call login
                case "3":
                    self.change_password() # call change password
                case "4":
                    self.school_info()
                case "5":
                    print("program exit....")
                    break # stop loop → exit program
                case _:
                    print("Invalid choice! Try again")
                    
# create school object
sc = School()

# start program
sc.school_menu()