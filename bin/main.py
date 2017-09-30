import sys,os
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(cur_path)
from modules import display
from modules import func,api
from public.template import *
from conf import settings



# global variety
auth_tool = dict(name = None,role = None)

def deco_login(role):
    def wrapper(fun):
        def inner(*args,**kwargs):
            auth_tool["role"] = role
            login()
            if auth_tool["name"]:
                fun(*args, **kwargs)
        return inner
    return wrapper


def login():
    flag = True
    while flag:
        IDs = api.find_data("users")
        print("all users:",IDs)
        print("current role:",auth_tool["role"])
        id = input("\033[1;34;1m Please input username:\033[0m").strip()
        psd = input("\033[1;34;1m Please input password:\033[0m").strip()
        if id in IDs:
            user_data = api.find_data("users", id)
            if psd == user_data["password"]:
                if user_data["role"] == auth_tool["role"]:
                    print("\033[1;34;1m Welcome, %s!\033[0m"%id)
                    api.logger("login").info("User %s login!" % id)
                    auth_tool["name"] = id
                    flag =False
                else:
                    print("\033[1;31;1m Role not match!\033[0m")
            else:
                print("\033[1;34;1m Password incorrect!\033[0m")
                api.logger("login").error("User %s password error input!" % id)
        else:
            print("\033[1;31;1m No such user!\033[0m")
            if auth_tool["role"] == 'students':
                ans = input("\033[1;34;1m Do you want to sign up?[y/n]:\033[0m")
                if ans == 'y':
                    username  = input("\033[1;34;1m Please input username:\033[0m").strip()
                    if username not in IDs:
                        psd = input("\033[1;34;1m Please input password:\033[0m").strip()
                        user_obj = People()
                        user_obj.name = username
                        user_obj.password = psd
                        user_obj.role = "students"
                        user_obj.renew()
                    else:
                        print("\033[1;31;1m This username has be signed!\033[0m")

                else:
                    exit("Bye...")


@deco_login("students")
def op_students():
    data = api.find_data("users", auth_tool["name"])
    student = People()
    student.name = data["name"]
    student.password = data["password"]
    student.role = data["role"]
    student.school = data["school"]
    student.classes = data["classes"]
    student.course = data["course"]
    student.money = data["money"]
    while True:
        choice = func.inpmsg(display.students,("1",'2','3','4'))
        if choice == '1':#Show My Info
            student.info()
        elif choice == '2':# Enroll
            student.enroll()
        elif choice == '3':#Learning
            student.learning()
        else:#back
            break
# class People():
#     def __init__(self):#default role
#         self.name = ''
#         self.password = ''
#         self.role = ''
#         self.school = ''
#         self.classes = ''
#         self.course = '' # stu can choose only one course
#         self.money = '10000'
@deco_login('teachers')
def op_teachers():
    data = api.find_data("users",auth_tool["name"])
    teacher = People()
    teacher.name = data["name"]
    teacher.password = data["password"]
    teacher.role = data["role"]
    teacher.school = data["school"]
    teacher.classes = data["classes"]
    teacher.course = data["course"]
    teacher.money = data["money"]
    while True:
        choice = func.inpmsg(display.teachers,("1",'2','3','4','5'))
        if choice == '1':#Show My Info
            teacher.info()
        elif choice == '2':# Enroll
            teacher.enroll()
        elif choice == '3':#Teaching
            teacher.teaching()
        elif choice == '4':#See Class Members
            teacher.show_member()
        else:# back
            break

@deco_login('admin')
def op_admin():
    admin = Admin()
    while True:
        choice = func.inpmsg(display.admin,("1",'2','3','4','5'))
        if choice == '1':#school
            admin.add_school()
        elif choice == '2':# classes
            admin.add_classes()
        elif choice == '3':#course
            admin.add_courses()
        elif choice == '4':#teacher
            admin.add_teachers()
        else:# back
            break



# main run

while True:
    choice = func.inpmsg(display.role,('1','2','3','q'))
    eval(display.entry[choice])





