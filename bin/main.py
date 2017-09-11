import sys,os
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(cur_path)
from modules import display
from modules import func

role_dic = {
    "1":'students',
    '2':'teachers',
    '3':'admin'
}
auth_tool = dict(name = None,role = None)

def auth_login(auth):
    def outer(func):
        def inner(*args,**kwargs):
            pass
        return inner
    return outer

@auth_login(auth_tool)
def op_student():
    #student operations
    pass
@auth_login(auth_tool)
def op_teacher():
    #teacher operations
    pass
@auth_login(auth_tool)
def op_admin():
    #admin operations
    pass

# main run

main_flag = True
while main_flag:
    choice = func.inpmsg(display.role,('1','2','3','q'))
    if choice == '1':#students
        op_student()
    elif choice == '2':#teachers
        op_teacher()
    else:#choice = '3' admin
        op_admin()
    break

