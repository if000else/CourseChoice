import sys,os
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(cur_path)
from modules import display
from modules import func,api
from public.template import *
from conf import settings



# global variety
auth_tool = dict(name = None,role = None)
def priority(auth,role):
    '''
    decorate for method of people class running
    :param auth:
    :param role:
    :return:
    '''
    def outer(fun):
        def inner(*args, **kwargs):
            if auth["role"] == role:
                fun(*args, **kwargs)
            else:
                api.logger("access").info(" user %s is denied!" % auth["name"])
        return inner
    return outer

def auth_login(role):
    def outer(fun):
        def inner(*args,**kwargs):
            name = func.login()
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

def op_students():
    auth_tool['role'] = 'students'
def op_teachers():
    auth_tool['role'] = 'teachers'
def op_admin():
    auth_tool['role'] = 'admin'

# main run

main_flag = True
while main_flag:
    choice = func.inpmsg(display.role,('1','2','3'))
    eval(display.entry[choice])






