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
            print("\033[1;33;1m Updating school:%s \033[0m"%self.name)
        else:
            print("\033[1;33;1m Creating new school named %s ...\033[0m" % self.name)
        with open(path,'wb') as f:
            data = dict(name = self.name,city = self.city,address = self.address)
            pickle.dump(data,f)

class Classes():
    '''
    a class accept only one teacher!
    '''
    def __init__(self,name,info,school,course,):
        self.name = name
        self.info = info # class info
        self.school = school #belong to which school
        self.course = course
        self.teachers = ''# only accept one teacher
        self.students =[]
    # @property
    # def teacher_in(self):
    #     return self.teachers
    #
    # @teacher_in.setter
    # def teacher_in(self,name):
    #     if not self.teachers:
    #         self.teachers.append(name)
    #         print("Wecome to class %s,teacher %s!"%(self.name,name))
    #     else:
    #         print("This class has exist a teacher!")

    # @property
    # def student_in(self):
    #     return self.students
    #
    # @student_in.setter
    # def student_in(self, name):
    #     self.teachers.append(name)
    #     print("Wecome to class %s,student %s!" % (self.name, name))


    def renew(self):
        data = dict(name=self.name,info=self.info,school=self.school,course=self.course,
                    teachers=self.teachers,students=self.students)
        path = "%s/classes/%s" % (settings.DateFile, self.name)
        if os.path.isfile(path): #already exist!
            # with open(path, 'ab') as f:
            #     pickle.dump(ban, f)
            print("\033[1;33;1m Updating %s classes\033[0m"%self.name)
        else:
            print("\033[1;33;1m Creating new class named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
                pickle.dump(data, f)

class Course():

    def __init__(self,name,info,price,school):
        self.name = name
        self.info = info
        self.price = price
        self.school = school
    def renew(self):
        data = dict(name=self.name,info=self.info,price=self.price,school=self.school)
        path = "%s/courses/%s" % (settings.DateFile, self.name)
        if os.path.isfile(path):
            print("\033[1;33;1m Updating %s course\033[0m" % self.name)
        else:
            print("\033[1;33;1m Creating new course named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
            pickle.dump(data, f)

class StudyRecord():
    '''
    record students' study and remarks
    '''

    def __init__(self,name,course):
        self.name = name
        self.time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.course = course
        # self.banji = class_obj.name
        self.grade = ''
        self.remark = ''

    @property
    def set_remark(self,):
        return self.remark
    @set_remark.setter
    def set_remark(self,string):
        self.remark = string
        print("New remark:",self.remark)

    @property
    def set_grade(self, ):
        return self.grade

    @set_grade.setter
    def set_grade(self, string):
        self.grade = string
        print("New grade:",self.grade)
    def renew(self):
        data=dict(time_str=self.time_str,name=self.name,course=self.course,
                  grade=self.grade,remark=self.remark)
        path = "%s/evaluations/%s" % (settings.DateFile,self.name)
        if os.path.isfile(path):
            print("\033[1;33;1m Updating %s record...\033[0m" % self.name)
        else:
            print("\033[1;33;1m Creating new record named %s ...\033[0m" % self.name)
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

    def info(self):
        '''
        show info
        :return:
        '''
        print('\033[1;33;1muser:%s role:%s \n school:%s class:%s\n course:%s  money:%s\033[0m'
              %(self.name,self.role,self.school,self.classes,self.course,self.money))

    def enroll(self):
        '''
        teachers or students enroll,choose school,course,then distribute a class,
        student must pay for the course
        :return:
        '''
        schools = api.find_data("schools") #load all files in schools dir
        courses = api.find_data("courses")
        classes = api.find_data("classes")
        if not self.school:# select school
            for item in schools:
                print(item)
            choice1 = input("\033[1;34;1mPlease choose schools:\033[0m").strip()
            if choice1 in schools:
                if not self.course:#select course
                    for item in courses:
                        c_data = api.find_data("courses", item)
                        if c_data["school"] == choice1:
                            print(c_data["name"])
                    choice2 = input("\033[1;34;1mPlease choose course:\033[0m").strip()
                    if choice2 in courses:
                        print("\033[1;33;1m Distributing classes...\033[0m")
                        time.sleep(2)
                        ban={}
                        for item in classes:
                            banji = api.find_data("classes", item)
                            if banji["course"] == choice2:  # find the class
                                ban = banji
                        if ban:
                            new_class = Classes(ban['name'], ban['info'],
                                                    ban["school"], ban["course"])
                            if self.role == "teachers":
                                if ban["teachers"]:
                                    print("\033[1;31;1m One teacher has choose the course!\033[0m")
                                else:
                                    self.school = choice1
                                    self.course = choice2
                                    self.classes = ban["name"]
                                    new_class.teachers = self.name
                                    new_class.renew()  # write in file
                                    self.renew()
                            elif self.role == "students":  # student must pay
                                price = float(api.find_data('courses', choice2)['price'])  # get price
                                balance = float(self.money)
                                result = balance - price
                                self.money = str(result)
                                print("\033[1;33;1m Current money: \033[0m", self.money)
                                self.classes = ban["name"]
                                self.school = choice1
                                self.course = choice2
                                new_class.students.append(self.name)
                                new_class.renew()
                                self.renew()
                                print(api.find_data("classes",new_class.name))
                        else:
                            print("\033[1;31;1mNo class open this course!\033[0m")
                    else:
                        print("\033[1;31;1m Invalid input! \033[0m")


            else:
                print("\033[1;31;1m Invalid input! \033[0m")
        else:
            print("\033[1;33;1m Already choose! \033[0m")


    def learning(self):
        '''
        having class then make remarks
        :return:
        '''
        if self.role == "students":#author
            if self.course:
                print("\033[1;34;1m Name: %s\nCourse:%s\nClass:%s \033[0m"
                      %(self.name,self.course,self.classes))
                print("\033[1;33;1mClass begin... \033[0m")
                time.sleep(3)
                print("\033[1;33;1mClass over...\033[0m")
                record = StudyRecord(self.name,self.course)
                words = input("How is the course?[low,mid,high]")
                record.set_remark = words
                record.renew()
            else:
                print("\033[1;31;1m Please enroll first!\033[0m")
        else:
            print("\033[1;31;1m Access is denied!\033[0m")
            api.logger("access").info("Reject user %s access! "%self.name)

    def teaching(self):
        '''
        teacher assess each student ,then give grade
        :return:
        '''
        if self.role == "teachers":
            if self.course:
                classdata = api.find_data("classes", self.classes)
                print(classdata)
                people = classdata["students"]
                print("\033[1;33;1m Name: %s\nCourse:%s\nClass:%s \033[0m"
                      % (self.name, self.course, self.classes))
                print("There are \033[1;33;1m%s \033[0m people in the class."%len(people))
                print("\033[1;33;1mClass begin... \033[0m")
                time.sleep(3)
                print("\033[1;33;1mClass over.Please assess each student:\033[0m")
                for student in people:
                    stu_date = api.find_data("evaluations",student)
                    if stu_date:
                        print("%s %s %s %s"%(stu_date["name"],stu_date["time_str"],
                                             stu_date["course"],stu_date["remark"]))
                        grade_obj = StudyRecord(stu_date["name"],stu_date["course"])
                        grade_obj.time_str = stu_date["time_str"]
                        grade_obj.remark = stu_date["remark"]
                        grade_obj.grade = input("\033[1;33;1mInput grade for student %s:\033[0m"%grade_obj.name)
                        grade_obj.renew()
            else:
                print("\033[1;31;1m Please enroll first!\033[0m")
        else:
            print("\033[1;31;1m Access is denied!\033[0m")
            api.logger("access").info("Reject user %s access! " % self.name)

    def show_member(self):
        if self.role == "teachers":
            if self.course:
                data = api.find_data("classes",self.classes) #list dir
                i = 1
                for item in data["students"]:
                    print("%s:\033[1;34;1m%s\033[0m record:%s"%(i,item,api.find_data("evaluations",item)))
                    i += 1
        else:
            print("\033[1;31;1m Access is denied!\033[0m")
            api.logger("access").info("Reject user %s access! " % self.name)

    def renew(self):
        path = "%s/users/%s" % (settings.DateFile, self.name)
        if os.path.isfile(path):  # already exist!
            print("\033[1;33;1m Updating  info of %s \033[0m"%self.name)
        else:
            print("\033[1;33;1m Creating new one named %s ...\033[0m" % self.name)
        with open(path, 'wb') as f:
            data = dict(name=self.name, password=self.password, role=self.role,
                        school=self.school, classes=self.classes, course=self.course, fee=self.money)
            pickle.dump(data, f)

class Admin():
    '''
    admin operations
    '''
    # def __init__(self,user):
    #     if user['role'] =='admin':
    #         self.data = user
    #     else:
    #         print("\033[1;31;1m Initializing user failed! \033[0m")
    def add_teachers(self):
        '''
        add a new teacher with initializing name,password,school
        :return:
        '''
        teacher = People()
        teacher.name = input("\033[1;33;1m Please input teacher name: \033[0m").strip()
        teacher.password = input("\033[1;33;1m Please input password: \033[0m").strip()
        teacher.role = "teachers"
        teacher.renew()
        # schools = api.find_data("schools")
        # if schools:
        #     for item in schools:
        #         print("School:",item)
        #     school = input("\033[1;33;1m Please select school \033[0m").strip()
        #     if school in schools:
        #         teacher.school = school
        #     teacher.role = "teachers"
        #     teacher.renew()
        # else:
        #     print("\033[1;31;1mPlease add schools first!\033[0m")

    def add_courses(self):
        '''
        add a new course with initializing name,info,price,school
        :return:
        '''
        schools = api.find_data("schools")
        if schools:
            for item in schools:
                print("\033[1;33;1mSchool:\033[0m", item)
            school = input("\033[1;33;1mPlease choose schools:\033[0m").strip()
            if school in schools:
                choice = input("\033[1;33;1mPlease input name,info,price in order:\033[0m").strip()
                choice = choice.split(',')
                course = Course(choice[0], choice[1], choice[2], school)
                course.renew()
            else:
                print("Invalid input")
        else:
            print("\033[1;31;1mPlease add  schools first!\033[0m")
    def add_classes(self):
        '''
        add a new class with initializing name,info,school,course
        :return:
        '''
        schools = api.find_data("schools")
        courses = api.find_data("courses")
        if schools and courses: #exist schools or courses
            for item in schools:
                print("\033[1;33;1mSchool:\033[0m", item)
            school = input("\033[1;33;1mPlease choose schools:\033[0m").strip()
            for item in courses:
                if api.find_data("courses",item)["school"] == school:
                    print(item)
            course = input("\033[1;33;1mPlease choose courses:\033[0m").strip()
            if school in schools and course in courses:
                className = input("\033[1;33;1mPlease input class name:\033[0m")
                classInfo = input(("\033[1;33;1mPlease input class description:\033[0m"))
                class_obj = Classes(className,classInfo,school,course)
                class_obj.renew()
            else:
                print("Invalid input")
        else:
            print("\033[1;31;1mPlease add courses or schools first!\033[0m")

    def add_school(self):
        '''
        add a new school with initializing name,city,address
        :return:
        '''
        data = api.find_data("schools")
        print("\033[1;33;1m Current schools:\033[0m")
        for item in data:
            print(api.find_data("schools", item))
        choice = input("\033[1;33;1m Input new school:name,city,address\033[0m").strip()
        try:
            lis = choice.split(",")
            school = School(lis[0], lis[1])
            school.address = lis[2]
            school.renew()
        except Exception as e:
            print(e)