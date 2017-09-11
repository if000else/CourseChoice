class School():
    def __init__(self,name,addr,city):
        self.name = name
        self.address = addr
        self.city = city


class Classes():
    def __init__(self,name,semester,date,school_obj):
        self.name = name
        self.semester = semester
        self.date = date # start date
        self.school = school_obj #belong to which school
    @property
    def teachers(self):
        '''
        reamin finishing...
        :return:
        '''
        print("there are many teachers:")
        return  None

    @teachers.setter  #ceate class
    def teachers(self,value):
        print("create teachers:",value)
    @property
    def students(self):
        return None

    @students.setter # create students
    def students(self,value):
        print("create students:",value)
class Course():
    def __init__(self,name,price,info,school_obj):
        self.name = name
        self.price = price
        self.info = info
        self.school = school_obj
class ClassRecord():
    def __init__(self,date,class_obj):
        self.date = date
        self.class_obj = class_obj
class StudyRecord():
    def __init__(self,date,grade,cRecord_obj,sign=True):
        self.date = date
        self.sign = sign
        self.grade = grade
        self.c_Record = cRecord_obj
class Student():
    def __init__(self,name,age,password,school_obj):
        self.name = name
        self.age = age
        self.password = password
        self.school = school_obj
