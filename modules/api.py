import os,logging,pickle
from conf import settings
# Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PathOfDate = os.path.join(Path,"data")
def find_data(folder,filename=None):
    '''
    load data ,return file data while filename exist,else return all filename in this dir.
    :param folder:
    :param filename:
    :return:
    '''
    url = "%s/%s"%(settings.DateFile,folder)
    find_all = os.listdir(url)
    if filename:
        if filename in find_all:
            file_path = '%s/%s'%(url,filename)
            with open(file_path,'rb') as f:
                find_one = pickle.load(f)
            return find_one
    else:
        return find_all



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
