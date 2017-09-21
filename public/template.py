import os,pickle,time
from conf import settings
from modules import api
# creating users must exclude users who have existed!
class School():
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.address = ''
        # self.banji = banji#list
        # self.course = course#list
        # self.teachers = teachers# list
        # self.students = students# list
    def renew(self):
        path = "%s/schools/%s"%(settings.DateFile,self.name)
        if os.path.isfile(path): #already exist!
            print("\033[1;33;1m updating school \033[0m",self.name)
        else:
            print("\033[1;33;1m creating new school named %s ...\033[0m" % self.name)
        with open(path,'wb') as f:
            data = dict(name = self.name,city = self.city,address = self.address)
            pickle.dump(data,f)


class Classes():
    '''
    info
    '''
    def __init__(self,name,info,school_obj,course_obj,):
        self.name = name
        self.info = info # class info
        self.school = school_obj.name #belong to which school
        self.course = course_obj.name
        self.teachers = []# only accept one teacher
        self.students =[]
    def renew(self):
        data = dict(name=self.name,info=self.info,school=self.school,course=self.course,
                    teachers=self.teachers,students=self.students)
        path = "%s/classes/%s" % (settings.DateFile, self.name)
        if os.path.isfile(path): #already exist!
            # with open(path, 'ab') as f:
            #     pickle.dump(ban, f)
            print("\033[1;33;1m updating %s classes\033[0m"%self.name)
        else:
            print("\033[1;33;1m creating new class named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
                pickle.dump(data, f)

class Course():

    def __init__(self,name,info,price,school_obj):
        self.name = name
        self.info = info
        self.price = price
        self.school = school_obj.name
    def renew(self):
        data = dict(name=self.name,info=self.info,price=self.price,school=self.school)
        path = "%s/courses/%s" % (settings.DateFile, self.name)
        if os.path.isfile(path):
            print("\033[1;33;1m updating %s course\033[0m" % self.name)
        else:
            print("\033[1;33;1m creating new course named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
            pickle.dump(data, f)


class StudyRecord():
    '''
    record students' study and remarks
    '''

    def __init__(self,name,course_obj,class_obj):
        self.name = name
        self.time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.course = course_obj.name
        self.banji = class_obj.name
        self.grade = ''
        self.remark = ''

    @property
    def set_remark(self,):
        return self.remark
    @set_remark.setter
    def set_remark(self,string):
        self.remark = string
        print("Your are modify remark...")

    @property
    def set_grade(self, ):
        return self.grade

    @set_grade.setter
    def set_grade(self, string):
        self.grade = string
        print("Your are modify grade...")
    def renew(self):
        data=dict(time_str=self.time_str,name=self.name,course=self.course,
                  banji=self.banji,grade=self.grade,remark=self.remark)
        path = "%s/evaluations/%s" % (settings.DateFile,self.name)
        if os.path.isfile(path):
            print("\033[1;33;1m updating %s record...\033[0m" % self.name)
        else:
            print("\033[1;33;1m creating new record named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
            pickle.dump(data, f)





class People():
    def __init__(self):#default role
        self.name = ''
        self.password = ''
        self.role = ''
        self.school = ''
        self.classes = ''
        self.course = '' # stu can choose only one course
        self.money = '10000'
    def show(self):
        print('user:%s,role:%s,\n school:%s,class:%s,course:%s \n money:%s'
              %(self.name,self.role,self.school,self.classes,self.course,self.money))

    def enroll(self):
        '''
        choose school,course,then pay for the course
        :return:
        '''
        schools = api.find_data("schools") #load all files in schools dir
        courses = api.find_data("courses")
        if not self.school:
            for sch in schools:
                print(api.find_data('schools',sch))
            choice = input("please choose schools:").strip()
            if choice in schools:
                self.school = choice
            else:
                print("\033[1;31;1m invalid input! \033[0m")
        else:
            print("\033[1;31;1m already exist! \033[0m")
        if not self.course:
            for cour in courses:
                print(api.find_data('courses', cour))
            choice = input("please choose courses:").strip()
            if choice in courses:
                self.course = choice
            else:
                print("\033[1;31;1m invalid input! \033[0m")
        else:
            print("\033[1;31;1m already exist! \033[0m")
        price = float(api.find_data('course',self.course)['price'])# get price
        balance = float(self.money)
        result = balance - price
        if result < 0:
            print("\033[1;31;1m money is not enough \033[0m")
        else:
            self.money = str(result)
            print("pay successfully,current money:",self.money)

        def renew(self):
            path = "%s/users/%s" % (settings.DateFile, self.name)
            if os.path.isfile(path):  # already exist!
                print("\033[1;33;1m updating  info of %s \033[0m", self.name)
            else:
                print("\033[1;33;1m creating new one named %s ...\033[0m" % self.name)
            with open(path, 'wb') as f:
                data = dict(name=self.name, password=self.password, role=self.role,
                            school=self.school, classes=self.classes, course=self.course, fee=self.money)
                pickle.dump(data, f)

# class Students(People):
#     def __init__(self):
#         People.__init__(self)
#
#
# class Teachers(People):
#     def __init__(self):
#         People.__init__()
#
#
# class Admin(People):
#     def __init__(self):
#         People.__init__()
#
#
