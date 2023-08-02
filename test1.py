import datetime
import os

# for windows
# boldRED = '\033[91m'
# lightGRN = '\033[92m'
# lightBLUE = '\033[94m'
# purple = '\033[95m'
# nc = '\033[0m'

# for linux
boldRED = '\033[1;31m'
lightGRN = '\033[1;32m'
lightBLUE = '\033[1;34m'
purple = '\033[0;35m'
nc = '\033[0m'

print(f"""{lightBLUE}
                               __                
 /\_|__|_ _ ._  _| _ ._  _ _  (_    __|_ _ ._ _  
/--\|_ |_(/_| |(_|(/_| |(_(/_ __)\/_> |_(/_| | | 
                                 /   {nc}{purple}Created By Jerrygems{nc}""")

users_txt = "users.txt"
students_attendance = "students_attendance.txt"
managers_attendance = "managers_attendance.txt"
admins_attendance = "admins_attendance.txt"
login=False
userInfo=None
userType="noBody"

def loginfn():
    input_username = input("[ENTER YOUR USERNAME]: ")
    input_password = input("[ENTER YOUR PASSWORD]: ")

    with open("users.txt", "r") as f:
        user_found = False  
        for line in f:
            name, age, username, password, user_type, date, time = line.strip().split(",")
            if input_username == username and input_password == password:
                global login, userInfo, userType
                userInfo = {
                    "name": name,
                    "age": int(age),
                    "username": username,
                    "password": password,
                    "userType": user_type,
                    "time": date,
                    "date": time
                }
                login = True
                userType = userInfo["userType"]
                print(f"Login Successful as {userType}")
                user_found = True
                break

        if not user_found:
            print("User does not exist or invalid credentials.")

def check_login():
    if (login==True) and (userType["userType"]!="noBody"):
        print(f"{lightGRN}Already Logged In as {userType}!{lightGRN}")
    else:
        inpt=input(f"{lightGRN}[noone is here wanna login right now]: (y/n) {nc}")
        if inpt=="y":
            loginfn()
        else:
            return
def check_admin():
    if userType=="admin":
        return True
    else:
        return False
    
def logout():
    global login,userType,userInfo
    login=False
    userInfo=None
    userType="noBody"

def mk_user(uType=None):
    print("Register User:")
    try:
        with open(users_txt, "a") as f:
            name = input("[ENTER YOUR NAME]: ")
            age = int(input("[ENTER AGE]: "))
            username = input("[ENTER YOUR USERNAME]: ")
            password = input("[ENTER YOUR PASSWORD]: ")
            if uType == "manager":
                userType = uType
            elif uType=="student":
                userType=uType
            else:
                userType = input("[ENTER TYPE OF USER]: ")
            day = datetime.datetime.now().strftime("%Y-%m-%d")
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            f.write(f"{name},{age},{username},{password},{userType},{day},{timestamp}\n")
            print("User Added Successfully")
    except Exception as exp:
        print(f"Error Occurred: {exp}")

def mark_attendance():
    if userType=="student":
        print(f"Mark Attendance for {userType}:")
        try:
            with open(students_attendance, "a") as f:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"{date},{time},{userInfo['username']},Present\n")
                print("Attendance Marked Successfully") 
        except Exception as exp:
            print(f"Error Occurred: {exp}")
    elif userType=="manager":
        print(f"Mark Attendance for {userType}:")
        try:
            with open(managers_attendance, "a") as f:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"{date},{time},{userInfo['username']},Present\n")
                print("Attendance Marked Successfully")
        except Exception as exp:
            print(f"Error Occurred: {exp}")
    elif userType=="admin":
        print(f"Mark Attendance for {userType}:")
        try:
            with open(admins_attendance, "a") as f:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"{date},{time},{userInfo['username']},Present\n")
                print("Attendance Marked Successfully")
        except Exception as exp:
            print(f"Error Occurred: {exp}")
    else:
        if login==False or userInfo==None or userType not in ["manager","admin","student"]:
            res=input(f"{boldRED}You're not Logged In{nc}\n{lightGRN}[WANNA LOGIN RIGHT NOW](y/n) :{nc}")
            if res=="y":
                loginfn()
            else:
                print(f"{purple}Alright you can login whenever you want.\nSee yah! ;-){nc}")
            
        else:
            print(f"{boldRED}[WARNING] Invalid User! {nc}")

def user_exists(uname=None, uType=None):
    with open("users.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[2] == uname and data[4] == uType:
                return True, data

    return False, None

def already_present():
    print('will do')

def creator():
    while True:
        inpt=input(f"{purple}for whom you wanna create?\n1. manager\n2. student\n3. exit\n{nc}")
        if inpt in ["manager","1"]:
            if userType=="admin":
                uType="manager"
                inp1 = input(f"{purple}1. create account\n\t\tOR\n2. create entry{nc}")
                if inp1 in ["1","create account","account"]:
                    mk_user(uType)
                elif inp1 in ["2","create entry", "entry"]:
                    try:
                        with open(managers_attendance, "a") as f:
                            username = input("[ENTER YOUR USERNAME]: ")
                            exists,data = user_exists(username,uType)
                            if exists==True:
                                date = datetime.datetime.now().strftime("%Y-%m-%d")
                                time = datetime.datetime.now().strftime("%H:%M:%S")
                                f.write(f"{date},{time},{data[2]},Present\n")
                                print("Attendance Marked Successfully")

                            else:
                                print(f"no such user with the type '{uType}' found!")
                    except Exception as exp:
                        print(f"Error Occurred: {exp}")
                elif inp1=="exit":
                    break
                else:
                    print("invalid option")
                    break
            else:
                print("this is only for admin")


        elif inpt in ["student","2"]:

            if userType in ["admin","manager"]:
                uType="student"
                inp1 = input(f"{purple}1. create account\n\t\tOR\n2. create entry{nc}")
                if inp1 in ["1","create account","account"]:
                    mk_user(uType)
                elif inp1 in ["2","create entry", "entry"]:
                    try:
                        with open(students_attendance, "a") as f:
                            username = input("[ENTER YOUR USERNAME]: ")
                            exists,data = user_exists(username,uType)
                            if exists==True:
                                date = datetime.datetime.now().strftime("%Y-%m-%d")
                                time = datetime.datetime.now().strftime("%H:%M:%S")
                                f.write(f"{date},{time},{data[2]},present\n")
                                print("Attendance Marked Successfully")

                            else:
                                print(f"no such user with the type '{uType}' found!")
                    except Exception as exp:
                        print(f"Error Occurred: {exp}")
            else:
                print("students can't run this this operation")
        elif inpt=="exit":
            break
        else:
            print(f"{boldRED}Please choose valid options{nc}")

def filteration_users(param=None):
    print("you are in filter mode : ")
    if param in ["name","1"]:
        name=input("Enter the name: ")
        with open(users_txt,"r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[2]==name:
                    print(f"{lightGRN}{data[0]}\t{data[1]}\t{data[2]}\t{data[4]}\t{data[5]}\t{data[6]}{nc}")
    elif param in ["type","2"]:
        type1=input("Enter the type from (student/manager/admin): ")
        if type1 in ["student","manager","admin"]:
            with open(users_txt,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[4]==type1:
                        print(f"{lightGRN}{data[0]}\t{data[1]}\t{data[2]}\t{data[4]}\t{data[5]}\t{data[6]}{nc}")
        else:
            print("invalid type!")

    elif param in ["date","3"]:
        date=input("Enter the date in this format(YYYY-MM-DD): ")
        with open(users_txt,"r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[5]==date:
                    print(f"{lightGRN}{data[0]}\t{data[1]}\t{data[2]}\t{data[4]}\t{data[5]}\t{data[6]}\t{nc}")
           
    elif param in ["age","4"]:
        age=input("Enter the age: ")
        with open(users_txt,"r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[1]==age:
                    print(f"{lightGRN}{data[0]}\t{data[1]}\t{data[2]}\t{data[4]}\t{data[5]}\t{data[6]}\t{nc}")
    else:
        return

def filteration_attendance(param=None,param2=None):
    print("\nyou are in filter mode : ")
    if param in ["name","1"]:
        name=input("Enter the name: ")
        with open(param2,"r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[2]==name:
                    print(f"{boldRED}{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}{nc}")
    elif param in ["type","2"]:
        para1=input("By (absent/present): ")
        if para1 in ["absent"]:
            with open(param2,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[4]==para1:
                        print(f"{boldRED}{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}{nc}")
        elif para1 in ["present"]:
            with open(param2,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[4]==para1:
                        print(f"{boldRED}{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}{nc}")
        else:
            print("invalid type!")

    elif param in ["date","3"]:
        date=input("Enter the date in this format(YYYY-MM-DD): ")
        with open(param2,"r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[5]==date:
                    print(f"{boldRED}{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}{nc}")
           
    else:
        return


def filtered_views():
    while True:
        print("\nyou can filter your views by any field")
        inp=input(f"{purple}so what you wanna filter?\n1. users list\n2. admins attendance\n3. managers attendance\n4. students attendace\n5. exit\n{nc}{lightBLUE}admin@attendance_system==>[input]: {nc}")
        if inp=="1":
            inpt=input(f"{purple}{'*'*20}\n1. name\n2. type\n3. date\n4. age\n5. exit\nby which parameter you wanna filter: {nc}")
            filteration_users(inpt)
        elif inp=="2":
            inpt=input(f"{purple}{'*'*20}\n1. name\n2. date\n3. presence\n4. exit\nby which parameter you wanna filter: {nc}")
            filteration_attendance(inpt,admins_attendance)
        elif inp=="3":
            inpt=input(f"{purple}{'*'*20}\n1. name\n2. type\n3. date\n4. exit\nby which parameter you wanna filter: {nc}")
            filteration_attendance(inpt,managers_attendance)
        elif inp=="4":
            inpt=input(f"{purple}{'*'*20}\n1. name\n2. type\n3. date\n4. exit\nby which parameter you wanna filter: {nc}")
            filteration_attendance(inpt,students_attendance)
        else:
            break
            

def view():
    while True:
        print("""what you want to view: \n1. users list\n2. managers attendance\n3. students attendance
4. filtered view\n5. exit""")
        inp=input("enter option number: ")
        if inp=="1":
            with open(users_txt,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    print(f"{lightGRN}{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}\t\t{data[4]}\t\t{data[5]}{nc}")
        elif inp=="2":
            with open(managers_attendance,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    print(f"{lightGRN}{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}{nc}")
        elif inp=="3":
            with open(students_attendance,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    print(f"{lightGRN}{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}{nc}")
        elif inp=="4":
            filtered_views()
        elif inp=="exit":
            break
        else:
            print(f"{boldRED}invalid command {nc}")
            break


def update():
    inp=input("which record you wanna edit or update\n1. users list\n2. managers attendance\n3. students attendace\n4. exit\n")
    if inp=="1":
        username_to_update = input("usernames are unique to by which we can easily find the field \nSo please the username to find the field : ")
        with open(users_txt, "r") as f:
            lines = f.readlines()
        entry_found = False
        with open(users_txt, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[2] == username_to_update:
                    print("Entry found! Choose what to update:\n1. Name\n2. Age\n3. Username\n4. Password\n5. User Type")
                    choice = input("Enter the number of the field you want to update from above: ")
                    if choice == "1":
                        inpr = input("Enter the new name: ")
                        data[0] = inpr
                    elif choice == "2":
                        inpr = input("Enter the new age: ")
                        data[1] = inpr
                    elif choice == "3":
                        inpr = input("Enter the new username: ")
                        data[2] = inpr
                    else:
                        print("Invalid choice. No entry updated.")
                        return
                    edited_line = ",".join(data) + "\n"
                    f.write(edited_line)
                    entry_found = True
                else:
                    f.write(line)
        if entry_found:
            print("Entry updated successfully!")
        else:
            print("Username not found. No entry updated.")
    elif inp=="2":
        username_to_update = input("usernames are unique to by which we can easily find the field \nSo please enter the username to find the field : ")
        with open(managers_attendance, "r") as f:
            lines = f.readlines()
        entry_found = False
        with open(managers_attendance, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[2] == username_to_update:
                    print("Entry found! Choose what to update:\n1. username\n2. availability\n3. date")
                    choice = input("Enter the number of the field you want to update: ")
                    if choice == "1":
                        inpr = input("Enter the new name: ")
                        data[2] = inpr
                    elif choice == "2":
                        inpr = input("Enter the new availability: ")
                        data[3] = inpr
                    elif choice == "3":
                        inpr = input("Enter the new 0:(YYYY-MM-DD) ")
                        data[0] = inpr
                    else:
                        print("Invalid choice. No entry updated.")
                        return
                    edited_line = ",".join(data) + "\n"
                    f.write(edited_line)
                    entry_found = True
                else:
                    f.write(line)
        if entry_found:
            print("Entry updated successfully!")
        else:
            print("Username not found. No entry updated.")
    elif inp=="3":
        username_to_update = input("usernames are unique to by which we can easily find the field \nSo please enter the username to find the field : ")
        with open(students_attendance, "r") as f:
            lines = f.readlines()
        entry_found = False
        with open(students_attendance, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[2] == username_to_update:
                    print("Entry found! Choose what to update:\n1. username\n2. availability\n3. date")
                    choice = input("Enter the number of the field you want to update: ")
                    if choice == "1":
                        inpr = input("Enter the new name: ")
                        data[2] = inpr
                    elif choice == "2":
                        inpr = input("Enter the new availability: ")
                        data[3] = inpr
                    elif choice == "3":
                        inpr = input("Enter the new 0:(YYYY-MM-DD) ")
                        data[0] = inpr
                    else:
                        print("Invalid choice. No entry updated.")
                        return
                    edited_line = ",".join(data) + "\n"
                    f.write(edited_line)
                    entry_found = True
                else:
                    f.write(line)
        if entry_found:
            print("Entry updated successfully!")
        else:
            print("Username not found. No entry updated.")
    else:
        print("")


def update_control():
    if userType in ["admin"]:
        update()
    else:
        print("managers and students are not allowed to user UPDATE operation")

def administrate():
    if userType in ["admin","manager"]:
        print(f"{purple}commands available:\n\t1. create\n\t2. view\n\t3. update\n\t{nc}")
        inp = input(f"{lightBLUE}admin@attendance_system==>{nc}")
        if inp=="create":
            creator()
        elif inp=="view":
            view()
        elif inp=="update":
            update_control()
    else:
        print(f"{boldRED}Noone Else can be here left admin and manager.\nBy The Way are you a hacker Who is tryna hack me hu...!")

def find_absentees(file_path, date):
    absentees = []
    with open("users.txt", "r") as users_file:
        users_data = users_file.readlines()
    with open(file_path, "r") as file:
        attendance_data = file.readlines()
    for user_line in users_data:
        user_info = user_line.strip().split(",")
        if len(user_info) != 7:
            continue
        name, age, username, password, userType, user_date, user_time = user_info
        if userType == "student":
            present = False
            for attendance_line in attendance_data:
                att_date, time, att_username, status = attendance_line.strip().split(",")
                if att_username == username and att_date == date and status == "Present":
                    present = True
                    break
            if not present:
                absentees.append(username)
    return absentees

    
# Main loop
while True:
    inp = input(f"{lightBLUE}jerrygems@attendance_system==>{nc}")
    if inp == "create user":
        result = check_admin()
        if result == True:
            mk_user()
        else:
            print('[HELP]: for this you can ask your admins')
    elif inp == "login":
        loginfn()
    elif inp == "mark attendance" or inp=="attend":
        mark_attendance()
    elif inp in ["CRUD","crud",]:
        administrate()
    elif inp == "logout":
        logout()
    elif inp == "status":
        print(f"userType={userType},userLogin={login}\n{lightGRN}Login User Info: \n{userInfo}{nc}")
    elif inp == "absentees":
        print("Select a file to check attendance from:\n1. Students Attendance\n2. Managers Attendance\n3. Admins Attendance")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            file = students_attendance
        elif choice == "2":
            file = managers_attendance
        elif choice == "3":
            file = admins_attendance
        else:
            print("Invalid choice. Please try again.")
            continue
        date_to_check = input("Enter the date to check for absentees (YYYY-MM-DD): ")
        absentees = find_absentees(file, date_to_check)
        if not absentees:
            print("No absentees found for the given date.")
        else:
            print("Absentees on", date_to_check, ":")
            for username in absentees:
                print(username)
    elif inp == "exit":
        break
    elif inp == "clear":
        os.system("clear")
    else:
        print("[Usage is given below]\n1. create user\n2. mark attendance\n3. status\n4. login\n5. logout\n6. CRUD \n10. exit")
