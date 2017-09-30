#CourseChoice System

##这是一个选课系统程序
### 作者介绍：

Author：Yaoqing Wang

Nickname:Huayiqiu

Blog:http://www.cnblogs.com/iforelse/

###功能使用介绍：

角色:学校、学员、课程、讲师

要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
6. 创建讲师角色时要关联学校， 
7. 提供角色接口
* 7.1 学员视图，可以注册， 交学费， 选择班级，
* 7.2 讲师视图，讲师可管理自己的班级， 上课时选择班级， 查     看班级学员列表 ， 修改所管理的学员的成绩 
* 7.3 管理视图，创建讲师， 创建班级，创建课程

8. 上面的操作产生的数据都通过pickle序列化保存到文件里

###目录结构：

`homework_ATM/`

`　　|-- bin/`

`　　　　| |-- main.py`

`　　|`

`　　|-- conf/`

`　　　　| |-- settings.py`

`　　|-- data/`

`　　　　|　|-- classes/`

`　　　　|　|-- courses/`

`　　　　|　|-- evaluations/`

`　　　　|　|-- schools/`

`　　　　|　|-- users/`

`　　　　|　|-- DataStructure.py/`

`　　　　| `

`　　|-- log/`

`　　　　|　|-- events.log/`


`　　　　| `

`　　|-- modules/`

`　　　　| |-- api.py`

`　　　　| |-- display.py`

`　　　　| |-- func.py`


`　　|`

`　　|-- public/`

`　　　　| |-- template.txt`

`　　　　|`


`　　|-- README`


###DateStructure:

school = '''
{name:'',city:'',address:''}
'''#dic

classes = '''
{name:'',info:'',school:'',course:'',teachers:[],students:[]}
'''#dic

course = '''
{name:'',info:'',price:'',school:'']}
'''#dic

studyrecord = '''
{time:'',name:'',course:'',grade:'',remark:''}
'''#dic

users = '''
{name: '',password:'',role:'',school:'',classes:'',course:'',money:''}
'''

 ###run:
 
 main()
 
 login in: admin 123456
 
 Notes: 
 
        Input in English is strongly recommend.
 
        All user's password is 123456
        