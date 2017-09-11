def colordisplay(string,arg):
    '''
    :param string: print strings with colors
    :param arg: red,green...
    :return:
    '''
    if arg == 'red':
     print("\033[1;31;1m%s\033[0m"%string)#红色
    elif arg == 'green':
     print("\033[1;32;1m%s\033[0m"%string)#绿色
    elif arg == 'yellow':
     print("\033[1;33;1m%s\033[0m"%string)#黄色
    elif arg == 'blue':
     print("\033[1;34;1m%s\033[0m"%string)#蓝色
    elif arg == 'purple':
     print("\033[1;34;1m%s\033[0m"%string)#紫色
    else:
     print("\033[1;30;1m%s\033[0m" %string)#白色
role = '''
Welcome To Course Choice System!
[1]. I am a student
[2]. I am a teacher
[3]. I am administrator
[q]. Quit
[choose the role you act as ] :

'''
students = '''
1. choose course
2. having class
3. my info
4. back

'''
teachers = '''
1. choose course
2. having class
3. my info
4. see my remarks
5. back
'''
admin = '''
1. create school
2. create class
3. create course
4. back
'''