import sys,os
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(cur_path)
from modules import display
from modules import func,api
from conf import settings



# universal variety
role_dic = {
    "1":'students',
    '2':'teachers',
    '3':'admin'
}
auth_tool = dict(name = None,role = None)
# log_student = api.logger("Students")
# log_teacher = api.logger("Teachers")
# log_admin = api.logger("admin")

def auth_login(auth,role):
    def outer(fun):
        def inner(*args,**kwargs):
            name = func.login(role)
            if name:
                auth['name'] = name
                auth['role'] = role
                if role == 'students':
                    api.logger("Students").info(" user %s login!"%name)
                elif role == 'teachers':
                    api.logger("Teachers").info("user %s login"%name)
                elif role == "admin":
                    api.logger("admin").info("user %s login"%name)
                fun(*args,**kwargs)
        return inner
    return outer

@auth_login(auth_tool,'students')
def op_student(auth):
    #student operations
    print(auth_tool)
@auth_login(auth_tool,'teachers')
def op_teacher(auth):
    print(auth_tool)
    #teacher operations
@auth_login(auth_tool,'admin')
def op_admin(auth):
    print(auth_tool)
    #admin operations


# main run

main_flag = True
while main_flag:
    choice = func.inpmsg(display.role,('1','2','3','4','q'))
    if choice == '1':#students
        op_student(auth_tool)
    elif choice == '2':#teachers
        op_teacher(auth_tool)
    elif choice == '3':#choice = '3' admin
        op_admin(auth_tool)
    else:# choice == '4' sign out
        if auth_tool['role'] == 'students':
            api.logger("Students").info(" user %s sign out!" % auth_tool['name'])
        elif auth_tool['role'] == 'teachers':
            api.logger("Teachers").info("user %s sign out" % auth_tool['name'])
        elif auth_tool['role'] == "admin":
            api.logger("admin").info("user %s sign out" % auth_tool['name'])
        auth_tool['name'] = None
        auth_tool['role'] = None





