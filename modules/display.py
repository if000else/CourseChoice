def colordisplay(*args):
    '''
    print strings with color input
    :param args: (string,color)
    :return:
    '''
    if args[1] == 'red':
     print("\033[1;31;1m%s\033[0m"%args[0])#red
    elif args[1] == 'green':
     print("\033[1;32;1m%s\033[0m"%args[0])#green
    elif args[1] == 'yellow':
     print("\033[1;33;1m%s\033[0m"%args[0])#yellow
    elif args[1] == 'blue':
     print("\033[1;34;1m%s\033[0m"%args[0])#blue
    elif args[1] == 'purple':
     print("\033[1;34;1m%s\033[0m"%args[0])#purple
    else:
     print("\033[1;30;1m%s\033[0m"%args[0])#white
role = '''
Welcome To Course Choice System!
[1]. I am a student
[2]. I am a teacher
[3]. I am administrator
[q]. Quit
Please choose :
'''
entry = {'1':"op_students()",
         '2':"op_teachers()",
         '3':"op_admin()",
         'q':"exit()"}

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
