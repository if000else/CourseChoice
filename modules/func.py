from modules import display,api
def inpmsg(message, limit_value=tuple()):
    '''
    inspect input message is valid or not
    :param message:sting type  to display
    :param limit_value:
    :return:input
    '''
    is_null_flag = True
    while is_null_flag:
        display.colordisplay(message, "blue")
        input_value = input().strip()
        if not input_value:
            display.colordisplay("Input is empty!", "red")
            continue
        elif input_value not in limit_value:
            display.colordisplay("Input is invalid,please retry!","red")
            continue
        else:
            if input_value == 'q':
                exit()
            return input_value


