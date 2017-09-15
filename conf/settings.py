import os
BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DateFile = os.path.join(BasePath,"data")
LogFile = os.path.join(BasePath,"logs")

LOG_LEVEL = 10#INFO

ROLE_LEVEL = {"students":"2","teachers":"1","admin":"0"}