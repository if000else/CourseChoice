import os
BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DateFile = os.path.join(BasePath,"data")
LogFile = os.path.join(BasePath,"logs")

LOG_LEVEL = 10#INFO

REMARK = {1:'low',
          2:'mid',
          3:'high'}


# print(os.listdir(DateFile)[0])