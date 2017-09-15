import os,logging
from conf import settings
# Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PathOfDate = os.path.join(Path,"data")
UserPath = '%s/user_info.txt'%settings.DateFile
def users_op(user,psd,op,admin='0'):
    '''
    read and write user info from/to file
    :param user:
    :param psd:
    :param op: flag "read" and "write"
    :param admin: flag
    :return:
    '''
    if op == 'write':#write request
        with open(UserPath,'a+') as f:
            f.write('%s,%s,%s\n'%(user,psd,admin))
            print("generate user successfully!")
        return None
    elif op=='read':#read request
        users = {}
        with open(UserPath,'r') as f:
            for line in f:
                item = line.strip().split(",")
                userdic = {item[0]:(item[1],item[2])}
                users.update(userdic)
        print(users)
        return users


import logging
def logger(log_type):
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(10)

    # create console handler and set level to debug

    if not logger.handlers:
        ch = logging.StreamHandler()  # print to screen
        ch.setLevel(10)
        # create file handler and set level to warning
        log_file = "events.log"
        fh = logging.FileHandler(log_file)#print to file
        fh.setLevel(10)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch and fh
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add ch and fh to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
